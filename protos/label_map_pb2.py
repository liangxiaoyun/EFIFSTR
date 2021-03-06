# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/label_map.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/label_map.proto',
  package='protos',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16protos/label_map.proto\x12\x06protos\"c\n\x08LabelMap\x12+\n\rcharacter_set\x18\x01 \x01(\x0b\x32\x14.protos.CharacterSet\x12\x17\n\x0clabel_offset\x18\x02 \x01(\x03:\x01\x30\x12\x11\n\tunk_label\x18\x03 \x01(\x03\"\xd3\x01\n\x0c\x43haracterSet\x12\x15\n\ttext_file\x18\x01 \x01(\t:\x00H\x00\x12\x17\n\x0btext_string\x18\x02 \x01(\t:\x00H\x00\x12\x42\n\x0c\x62uilt_in_set\x18\x03 \x01(\x0e\x32\x1f.protos.CharacterSet.BuiltInSet:\tLOWERCASEH\x00\"?\n\nBuiltInSet\x12\r\n\tLOWERCASE\x10\x00\x12\x0c\n\x08\x41LLCASES\x10\x01\x12\x14\n\x10\x41LLCASES_SYMBOLS\x10\x02\x42\x0e\n\x0csource_oneof'
)



_CHARACTERSET_BUILTINSET = _descriptor.EnumDescriptor(
  name='BuiltInSet',
  full_name='protos.CharacterSet.BuiltInSet',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LOWERCASE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALLCASES', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALLCASES_SYMBOLS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=268,
  serialized_end=331,
)
_sym_db.RegisterEnumDescriptor(_CHARACTERSET_BUILTINSET)


_LABELMAP = _descriptor.Descriptor(
  name='LabelMap',
  full_name='protos.LabelMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='character_set', full_name='protos.LabelMap.character_set', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label_offset', full_name='protos.LabelMap.label_offset', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unk_label', full_name='protos.LabelMap.unk_label', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=34,
  serialized_end=133,
)


_CHARACTERSET = _descriptor.Descriptor(
  name='CharacterSet',
  full_name='protos.CharacterSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text_file', full_name='protos.CharacterSet.text_file', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text_string', full_name='protos.CharacterSet.text_string', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='built_in_set', full_name='protos.CharacterSet.built_in_set', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CHARACTERSET_BUILTINSET,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='source_oneof', full_name='protos.CharacterSet.source_oneof',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=136,
  serialized_end=347,
)

_LABELMAP.fields_by_name['character_set'].message_type = _CHARACTERSET
_CHARACTERSET.fields_by_name['built_in_set'].enum_type = _CHARACTERSET_BUILTINSET
_CHARACTERSET_BUILTINSET.containing_type = _CHARACTERSET
_CHARACTERSET.oneofs_by_name['source_oneof'].fields.append(
  _CHARACTERSET.fields_by_name['text_file'])
_CHARACTERSET.fields_by_name['text_file'].containing_oneof = _CHARACTERSET.oneofs_by_name['source_oneof']
_CHARACTERSET.oneofs_by_name['source_oneof'].fields.append(
  _CHARACTERSET.fields_by_name['text_string'])
_CHARACTERSET.fields_by_name['text_string'].containing_oneof = _CHARACTERSET.oneofs_by_name['source_oneof']
_CHARACTERSET.oneofs_by_name['source_oneof'].fields.append(
  _CHARACTERSET.fields_by_name['built_in_set'])
_CHARACTERSET.fields_by_name['built_in_set'].containing_oneof = _CHARACTERSET.oneofs_by_name['source_oneof']
DESCRIPTOR.message_types_by_name['LabelMap'] = _LABELMAP
DESCRIPTOR.message_types_by_name['CharacterSet'] = _CHARACTERSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LabelMap = _reflection.GeneratedProtocolMessageType('LabelMap', (_message.Message,), {
  'DESCRIPTOR' : _LABELMAP,
  '__module__' : 'protos.label_map_pb2'
  # @@protoc_insertion_point(class_scope:protos.LabelMap)
  })
_sym_db.RegisterMessage(LabelMap)

CharacterSet = _reflection.GeneratedProtocolMessageType('CharacterSet', (_message.Message,), {
  'DESCRIPTOR' : _CHARACTERSET,
  '__module__' : 'protos.label_map_pb2'
  # @@protoc_insertion_point(class_scope:protos.CharacterSet)
  })
_sym_db.RegisterMessage(CharacterSet)


# @@protoc_insertion_point(module_scope)
