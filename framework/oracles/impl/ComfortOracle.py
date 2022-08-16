import math
from typing import List, Optional
from framework.oracles.OracleInterface import OracleInterface
from modules.localization.proto.localization_pb2 import LocalizationEstimate
import numpy as np


class ComfortOracle(OracleInterface):
    prev_: Optional[LocalizationEstimate]
    next_: Optional[LocalizationEstimate]
    accl: List[float]

    MAX_ACCL = 4.0
    MAX_DCCL = -4.0

    def __init__(self) -> None:
        self.prev_ = None
        self.next_ = None
        self.accl = list()

    def get_interested_topics(self):
        return ['/apollo/localization/pose']

    def on_new_message(self, topic: str, message, t):
        if self.prev_ is None and self.next_ is None:
            self.prev_ = message
            return
        self.next_ = message
        # compare velocity
        prev_velocity = self.calculate_velocity(
            self.prev_.pose.linear_velocity)
        next_velocity = self.calculate_velocity(
            self.next_.pose.linear_velocity)

        delta_t = self.next_.header.timestamp_sec - self.prev_.header.timestamp_sec
        delta_v = next_velocity - prev_velocity
        accel = round(delta_v / delta_t, 1)
        self.accl.append(accel)

        # update prev_
        self.prev_ = message

    def calculate_velocity(self, linear_velocity):
        x, y, z = linear_velocity.x, linear_velocity.y, linear_velocity.z
        return math.sqrt(x**2+y**2)

    def get_result(self):
        result = list()
        max_accl = np.max(self.accl)
        min_accl = np.min(self.accl)
        if max_accl > ComfortOracle.MAX_ACCL:
            result.append(('comfort', 'Acceleratoin exceeded max'))
        if min_accl < ComfortOracle.MAX_DCCL:
            result.append(('comfort', 'Deceleration exceeded max'))
        return result