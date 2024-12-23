# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/common/configs/proto/vehicle_config.proto

import sys

_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from modules.common.proto import \
    geometry_pb2 as modules_dot_common_dot_proto_dot_geometry__pb2
from modules.common.proto import \
    header_pb2 as modules_dot_common_dot_proto_dot_header__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/common/configs/proto/vehicle_config.proto',
  package='apollo.common',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n1modules/common/configs/proto/vehicle_config.proto\x12\rapollo.common\x1a!modules/common/proto/header.proto\x1a#modules/common/proto/geometry.proto\"\x91\x01\n\tTransform\x12\x14\n\x0csource_frame\x18\x01 \x01(\x0c\x12\x14\n\x0ctarget_frame\x18\x02 \x01(\x0c\x12+\n\x0btranslation\x18\x03 \x01(\x0b\x32\x16.apollo.common.Point3D\x12+\n\x08rotation\x18\x04 \x01(\x0b\x32\x19.apollo.common.Quaternion\"9\n\nExtrinsics\x12+\n\ttansforms\x18\x01 \x03(\x0b\x32\x18.apollo.common.Transform\"@\n\tVehicleID\x12\x0b\n\x03vin\x18\x01 \x01(\t\x12\r\n\x05plate\x18\x02 \x01(\t\x12\x17\n\x0fother_unique_id\x18\x03 \x01(\t\"^\n\x0cLatencyParam\x12\x11\n\tdead_time\x18\x01 \x01(\x01\x12\x11\n\trise_time\x18\x02 \x01(\x01\x12\x11\n\tpeak_time\x18\x03 \x01(\x01\x12\x15\n\rsettling_time\x18\x04 \x01(\x01\"\xe0\x06\n\x0cVehicleParam\x12*\n\x05\x62rand\x18\x01 \x01(\x0e\x32\x1b.apollo.common.VehicleBrand\x12,\n\nvehicle_id\x18\x02 \x01(\x0b\x32\x18.apollo.common.VehicleID\x12!\n\x14\x66ront_edge_to_center\x18\x03 \x01(\x01:\x03nan\x12 \n\x13\x62\x61\x63k_edge_to_center\x18\x04 \x01(\x01:\x03nan\x12 \n\x13left_edge_to_center\x18\x05 \x01(\x01:\x03nan\x12!\n\x14right_edge_to_center\x18\x06 \x01(\x01:\x03nan\x12\x13\n\x06length\x18\x07 \x01(\x01:\x03nan\x12\x12\n\x05width\x18\x08 \x01(\x01:\x03nan\x12\x13\n\x06height\x18\t \x01(\x01:\x03nan\x12\x1c\n\x0fmin_turn_radius\x18\n \x01(\x01:\x03nan\x12\x1d\n\x10max_acceleration\x18\x0b \x01(\x01:\x03nan\x12\x1d\n\x10max_deceleration\x18\x0c \x01(\x01:\x03nan\x12\x1c\n\x0fmax_steer_angle\x18\r \x01(\x01:\x03nan\x12!\n\x14max_steer_angle_rate\x18\x0e \x01(\x01:\x03nan\x12!\n\x14min_steer_angle_rate\x18\x0f \x01(\x01:\x03nan\x12\x18\n\x0bsteer_ratio\x18\x10 \x01(\x01:\x03nan\x12\x17\n\nwheel_base\x18\x11 \x01(\x01:\x03nan\x12!\n\x14wheel_rolling_radius\x18\x12 \x01(\x01:\x03nan\x12\'\n\x1amax_abs_speed_when_stopped\x18\x13 \x01(\x02:\x03nan\x12\x1b\n\x0e\x62rake_deadzone\x18\x14 \x01(\x01:\x03nan\x12\x1e\n\x11throttle_deadzone\x18\x15 \x01(\x01:\x03nan\x12;\n\x16steering_latency_param\x18\x16 \x01(\x0b\x32\x1b.apollo.common.LatencyParam\x12;\n\x16throttle_latency_param\x18\x17 \x01(\x0b\x32\x1b.apollo.common.LatencyParam\x12\x38\n\x13\x62rake_latency_param\x18\x18 \x01(\x0b\x32\x1b.apollo.common.LatencyParam\"\x99\x01\n\rVehicleConfig\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.apollo.common.Header\x12\x32\n\rvehicle_param\x18\x02 \x01(\x0b\x32\x1b.apollo.common.VehicleParam\x12-\n\nextrinsics\x18\x03 \x01(\x0b\x32\x19.apollo.common.Extrinsics*~\n\x0cVehicleBrand\x12\x0f\n\x0bLINCOLN_MKZ\x10\x00\x12\x07\n\x03GEM\x10\x01\x12\t\n\x05LEXUS\x10\x02\x12\x0b\n\x07TRANSIT\x10\x03\x12\x07\n\x03GE3\x10\x04\x12\x07\n\x03WEY\x10\x05\x12\x0c\n\x08ZHONGYUN\x10\x06\x12\x06\n\x02\x43H\x10\x07\x12\x08\n\x04\x44KIT\x10\x08\x12\n\n\x06NEOLIX\x10\t')
  ,
  dependencies=[modules_dot_common_dot_proto_dot_header__pb2.DESCRIPTOR,modules_dot_common_dot_proto_dot_geometry__pb2.DESCRIPTOR,])

_VEHICLEBRAND = _descriptor.EnumDescriptor(
  name='VehicleBrand',
  full_name='apollo.common.VehicleBrand',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LINCOLN_MKZ', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GEM', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEXUS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRANSIT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GE3', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WEY', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZHONGYUN', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CH', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DKIT', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEOLIX', index=9, number=9,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1532,
  serialized_end=1658,
)
_sym_db.RegisterEnumDescriptor(_VEHICLEBRAND)

VehicleBrand = enum_type_wrapper.EnumTypeWrapper(_VEHICLEBRAND)
LINCOLN_MKZ = 0
GEM = 1
LEXUS = 2
TRANSIT = 3
GE3 = 4
WEY = 5
ZHONGYUN = 6
CH = 7
DKIT = 8
NEOLIX = 9



_TRANSFORM = _descriptor.Descriptor(
  name='Transform',
  full_name='apollo.common.Transform',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_frame', full_name='apollo.common.Transform.source_frame', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_frame', full_name='apollo.common.Transform.target_frame', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='translation', full_name='apollo.common.Transform.translation', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rotation', full_name='apollo.common.Transform.rotation', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=286,
)


_EXTRINSICS = _descriptor.Descriptor(
  name='Extrinsics',
  full_name='apollo.common.Extrinsics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tansforms', full_name='apollo.common.Extrinsics.tansforms', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=288,
  serialized_end=345,
)


_VEHICLEID = _descriptor.Descriptor(
  name='VehicleID',
  full_name='apollo.common.VehicleID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vin', full_name='apollo.common.VehicleID.vin', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='plate', full_name='apollo.common.VehicleID.plate', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='other_unique_id', full_name='apollo.common.VehicleID.other_unique_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=347,
  serialized_end=411,
)


_LATENCYPARAM = _descriptor.Descriptor(
  name='LatencyParam',
  full_name='apollo.common.LatencyParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dead_time', full_name='apollo.common.LatencyParam.dead_time', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rise_time', full_name='apollo.common.LatencyParam.rise_time', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='peak_time', full_name='apollo.common.LatencyParam.peak_time', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='settling_time', full_name='apollo.common.LatencyParam.settling_time', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=413,
  serialized_end=507,
)


_VEHICLEPARAM = _descriptor.Descriptor(
  name='VehicleParam',
  full_name='apollo.common.VehicleParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='brand', full_name='apollo.common.VehicleParam.brand', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vehicle_id', full_name='apollo.common.VehicleParam.vehicle_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='front_edge_to_center', full_name='apollo.common.VehicleParam.front_edge_to_center', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='back_edge_to_center', full_name='apollo.common.VehicleParam.back_edge_to_center', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left_edge_to_center', full_name='apollo.common.VehicleParam.left_edge_to_center', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right_edge_to_center', full_name='apollo.common.VehicleParam.right_edge_to_center', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length', full_name='apollo.common.VehicleParam.length', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='apollo.common.VehicleParam.width', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='apollo.common.VehicleParam.height', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_turn_radius', full_name='apollo.common.VehicleParam.min_turn_radius', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_acceleration', full_name='apollo.common.VehicleParam.max_acceleration', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_deceleration', full_name='apollo.common.VehicleParam.max_deceleration', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_steer_angle', full_name='apollo.common.VehicleParam.max_steer_angle', index=12,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_steer_angle_rate', full_name='apollo.common.VehicleParam.max_steer_angle_rate', index=13,
      number=14, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_steer_angle_rate', full_name='apollo.common.VehicleParam.min_steer_angle_rate', index=14,
      number=15, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='steer_ratio', full_name='apollo.common.VehicleParam.steer_ratio', index=15,
      number=16, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wheel_base', full_name='apollo.common.VehicleParam.wheel_base', index=16,
      number=17, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wheel_rolling_radius', full_name='apollo.common.VehicleParam.wheel_rolling_radius', index=17,
      number=18, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_abs_speed_when_stopped', full_name='apollo.common.VehicleParam.max_abs_speed_when_stopped', index=18,
      number=19, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='brake_deadzone', full_name='apollo.common.VehicleParam.brake_deadzone', index=19,
      number=20, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='throttle_deadzone', full_name='apollo.common.VehicleParam.throttle_deadzone', index=20,
      number=21, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=(1e10000 * 0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='steering_latency_param', full_name='apollo.common.VehicleParam.steering_latency_param', index=21,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='throttle_latency_param', full_name='apollo.common.VehicleParam.throttle_latency_param', index=22,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='brake_latency_param', full_name='apollo.common.VehicleParam.brake_latency_param', index=23,
      number=24, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=510,
  serialized_end=1374,
)


_VEHICLECONFIG = _descriptor.Descriptor(
  name='VehicleConfig',
  full_name='apollo.common.VehicleConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='apollo.common.VehicleConfig.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vehicle_param', full_name='apollo.common.VehicleConfig.vehicle_param', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extrinsics', full_name='apollo.common.VehicleConfig.extrinsics', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1377,
  serialized_end=1530,
)

_TRANSFORM.fields_by_name['translation'].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._POINT3D
_TRANSFORM.fields_by_name['rotation'].message_type = modules_dot_common_dot_proto_dot_geometry__pb2._QUATERNION
_EXTRINSICS.fields_by_name['tansforms'].message_type = _TRANSFORM
_VEHICLEPARAM.fields_by_name['brand'].enum_type = _VEHICLEBRAND
_VEHICLEPARAM.fields_by_name['vehicle_id'].message_type = _VEHICLEID
_VEHICLEPARAM.fields_by_name['steering_latency_param'].message_type = _LATENCYPARAM
_VEHICLEPARAM.fields_by_name['throttle_latency_param'].message_type = _LATENCYPARAM
_VEHICLEPARAM.fields_by_name['brake_latency_param'].message_type = _LATENCYPARAM
_VEHICLECONFIG.fields_by_name['header'].message_type = modules_dot_common_dot_proto_dot_header__pb2._HEADER
_VEHICLECONFIG.fields_by_name['vehicle_param'].message_type = _VEHICLEPARAM
_VEHICLECONFIG.fields_by_name['extrinsics'].message_type = _EXTRINSICS
DESCRIPTOR.message_types_by_name['Transform'] = _TRANSFORM
DESCRIPTOR.message_types_by_name['Extrinsics'] = _EXTRINSICS
DESCRIPTOR.message_types_by_name['VehicleID'] = _VEHICLEID
DESCRIPTOR.message_types_by_name['LatencyParam'] = _LATENCYPARAM
DESCRIPTOR.message_types_by_name['VehicleParam'] = _VEHICLEPARAM
DESCRIPTOR.message_types_by_name['VehicleConfig'] = _VEHICLECONFIG
DESCRIPTOR.enum_types_by_name['VehicleBrand'] = _VEHICLEBRAND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Transform = _reflection.GeneratedProtocolMessageType('Transform', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFORM,
  __module__ = 'modules.common.configs.proto.vehicle_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.common.Transform)
  ))
_sym_db.RegisterMessage(Transform)

Extrinsics = _reflection.GeneratedProtocolMessageType('Extrinsics', (_message.Message,), dict(
  DESCRIPTOR = _EXTRINSICS,
  __module__ = 'modules.common.configs.proto.vehicle_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.common.Extrinsics)
  ))
_sym_db.RegisterMessage(Extrinsics)

VehicleID = _reflection.GeneratedProtocolMessageType('VehicleID', (_message.Message,), dict(
  DESCRIPTOR = _VEHICLEID,
  __module__ = 'modules.common.configs.proto.vehicle_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.common.VehicleID)
  ))
_sym_db.RegisterMessage(VehicleID)

LatencyParam = _reflection.GeneratedProtocolMessageType('LatencyParam', (_message.Message,), dict(
  DESCRIPTOR = _LATENCYPARAM,
  __module__ = 'modules.common.configs.proto.vehicle_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.common.LatencyParam)
  ))
_sym_db.RegisterMessage(LatencyParam)

VehicleParam = _reflection.GeneratedProtocolMessageType('VehicleParam', (_message.Message,), dict(
  DESCRIPTOR = _VEHICLEPARAM,
  __module__ = 'modules.common.configs.proto.vehicle_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.common.VehicleParam)
  ))
_sym_db.RegisterMessage(VehicleParam)

VehicleConfig = _reflection.GeneratedProtocolMessageType('VehicleConfig', (_message.Message,), dict(
  DESCRIPTOR = _VEHICLECONFIG,
  __module__ = 'modules.common.configs.proto.vehicle_config_pb2'
  # @@protoc_insertion_point(class_scope:apollo.common.VehicleConfig)
  ))
_sym_db.RegisterMessage(VehicleConfig)


# @@protoc_insertion_point(module_scope)
