from logging import Logger
import time
from typing import List, Optional, Set, Tuple
from apollo.CyberBridge import Topics
from apollo.ApolloContainer import ApolloContainer
from map.utils import get_coordinate_for, get_lane_by_id
from modules.common.proto.header_pb2 import Header
from modules.localization.proto.localization_pb2 import LocalizationEstimate
from modules.localization.proto.pose_pb2 import Pose
from modules.map.proto.map_pb2 import Map
from modules.planning.proto.planning_pb2 import ADCTrajectory
from modules.routing.proto.routing_pb2 import LaneWaypoint, RoutingRequest
from utils import zero_velocity, get_logger
from config import USE_SIM_CONTROL_STANDALONE
from apollo.utils import PositionEstimate, extract_main_decision


class ApolloRunner:
    logger: Logger
    nid: int
    container: ApolloContainer
    map: Map
    start: PositionEstimate
    start_time: float
    destination: PositionEstimate

    routing_started: bool
    stop_time_counter: float
    localization: Optional[LocalizationEstimate]
    planning: Optional[ADCTrajectory]
    __min_distance: Optional[float]
    __decisions: Set[Tuple]
    __coords: List[Tuple]

    def __init__(self,
                 nid: int,
                 ctn: ApolloContainer,
                 map: Map,
                 start: PositionEstimate,
                 start_time: float,
                 destination: PositionEstimate
                 ) -> None:
        self.logger = get_logger(f'ApolloRunner[{ctn.container_name}]')
        self.nid = nid
        self.container = ctn
        self.map = map
        self.start = start
        self.start_time = start_time
        self.destination = destination

    def set_min_distance(self, d: float):
        if self.__min_distance is None:
            self.__min_distance = d
        elif d < self.__min_distance:
            self.__min_distance = d

    def register_publishers(self):
        for c in [Topics.Localization, Topics.Obstacles, Topics.TrafficLight, Topics.RoutingRequest]:
            self.container.bridge.add_publisher(c)

    def register_subscribers(self):

        def lcb(data):
            prev_ = self.localization
            next_ = data

            if prev_ != None and \
                prev_.header.module_name == "SimControl" and \
                    next_.header.module_name == "SimControl" and \
                self.routing_started:
                prev_stop = zero_velocity(prev_.pose.linear_velocity)
                next_stop = zero_velocity(next_.pose.linear_velocity)

                if prev_stop and next_stop:
                    tdelta = next_.header.timestamp_sec - prev_.header.timestamp_sec
                    stop_time = self.stop_time_counter
                    new_time = stop_time + tdelta
                    self.stop_time_counter = new_time
                else:
                    self.stop_time_counter = 0

            self.localization = data
            self.__coords.append((data.pose.position.x, data.pose.position.y))

        def pcb(data):
            self.planning = data
            decisions = extract_main_decision(data)
            self.__decisions.update(decisions)

        self.container.bridge.add_subscriber(Topics.Localization, lcb)
        self.container.bridge.add_subscriber(Topics.Planning, pcb)

    def initialize(self):
        '''
            Reset data, stop running modules, stop sim control
            send localization, restart sim control, restart running modules
        '''
        self.logger.debug(
            f'Initializing container {self.container.container_name}')

        # initialize container
        self.container.reset()
        self.register_publishers()
        self.send_initial_localization()
        if not USE_SIM_CONTROL_STANDALONE:
            self.container.dreamview.start_sim_control()

        # initialize class variables
        self.routing_started = False
        self.__min_distance = None
        self.__decisions = set()
        self.__coords = list()
        self.stop_time_counter = 0.0
        self.planning = None
        self.localization = None
        self.register_subscribers()

        self.container.bridge.spin()

        self.logger.debug(
            f'Initialized container {self.container.container_name}')

    def should_send_routing(self, t: float):
        return t >= self.start_time and not self.routing_started

    def send_initial_localization(self):
        self.logger.debug('Sending initial localization')
        coord, heading = get_coordinate_for(get_lane_by_id(
            self.map, self.start.lane_id), self.start.s)

        loc = LocalizationEstimate(
            header=Header(
                timestamp_sec=time.time(),
                module_name="MAGGIE",
                sequence_num=0
            ),
            pose=Pose(
                position=coord,
                heading=heading,
            )
        )
        for i in range(4):
            loc.header.sequence_num = i
            self.container.bridge.publish(
                Topics.Localization, loc.SerializeToString())
            time.sleep(0.5)

    def send_routing(self):
        self.logger.debug(
            f'Sending routing request to {self.container.container_name}')
        self.routing_started = True

        coord, heading = get_coordinate_for(get_lane_by_id(
            self.map, self.start.lane_id), self.start.s)

        rr = RoutingRequest(
            header=Header(
                timestamp_sec=time.time(),
                module_name="MAGGIE",
                sequence_num=0
            ),
            waypoint=[
                LaneWaypoint(
                    pose=coord,
                    heading=heading
                ),
                LaneWaypoint(
                    id=self.destination.lane_id,
                    s=self.destination.s,
                )
            ]
        )

        self.container.bridge.publish(
            Topics.RoutingRequest, rr.SerializeToString()
        )

    def stop(self, stop_reason: str):
        self.logger.debug('Stopping container')
        self.container.stop_all()
        self.logger.debug(f"STOPPED [{stop_reason}]")

    def get_min_distance(self):
        return self.__min_distance

    def get_decisions(self):
        return self.__decisions

    def get_trajectory(self):
        return self.__coords