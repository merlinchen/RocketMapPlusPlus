# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/get_holo_inventory_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/get_holo_inventory_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nHpogoprotos/networking/requests/messages/get_holo_inventory_message.proto\x12\'pogoprotos.networking.requests.messages\"L\n\x17GetHoloInventoryMessage\x12\x19\n\x11last_timestamp_ms\x18\x01 \x01(\x03\x12\x16\n\x0eitem_been_seen\x18\x02 \x01(\x05\x62\x06proto3')
)




_GETHOLOINVENTORYMESSAGE = _descriptor.Descriptor(
  name='GetHoloInventoryMessage',
  full_name='pogoprotos.networking.requests.messages.GetHoloInventoryMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='last_timestamp_ms', full_name='pogoprotos.networking.requests.messages.GetHoloInventoryMessage.last_timestamp_ms', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_been_seen', full_name='pogoprotos.networking.requests.messages.GetHoloInventoryMessage.item_been_seen', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=193,
)

DESCRIPTOR.message_types_by_name['GetHoloInventoryMessage'] = _GETHOLOINVENTORYMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetHoloInventoryMessage = _reflection.GeneratedProtocolMessageType('GetHoloInventoryMessage', (_message.Message,), dict(
  DESCRIPTOR = _GETHOLOINVENTORYMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.get_holo_inventory_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.GetHoloInventoryMessage)
  ))
_sym_db.RegisterMessage(GetHoloInventoryMessage)


# @@protoc_insertion_point(module_scope)
