# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/bidirectional_rnn.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos import rnn_cell_pb2 as protos_dot_rnn__cell__pb2
from protos import hyperparams_pb2 as protos_dot_hyperparams__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/bidirectional_rnn.proto',
  package='protos',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1eprotos/bidirectional_rnn.proto\x12\x06protos\x1a\x15protos/rnn_cell.proto\x1a\x18protos/hyperparams.proto\"\xef\x01\n\x10\x42idirectionalRnn\x12\x14\n\x06static\x18\x01 \x01(\x08:\x04true\x12\'\n\x0e\x66w_bw_rnn_cell\x18\x02 \x01(\x0b\x32\x0f.protos.RnnCell\x12,\n\x0frnn_regularizer\x18\x03 \x01(\x0b\x32\x13.protos.Regularizer\x12\x1b\n\x10num_output_units\x18\x04 \x01(\x05:\x01\x30\x12+\n\x0e\x66\x63_hyperparams\x18\x05 \x01(\x0b\x32\x13.protos.Hyperparams\x12$\n\x15summarize_activations\x18\x06 \x01(\x08:\x05\x66\x61lse'
  ,
  dependencies=[protos_dot_rnn__cell__pb2.DESCRIPTOR,protos_dot_hyperparams__pb2.DESCRIPTOR,])




_BIDIRECTIONALRNN = _descriptor.Descriptor(
  name='BidirectionalRnn',
  full_name='protos.BidirectionalRnn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='static', full_name='protos.BidirectionalRnn.static', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fw_bw_rnn_cell', full_name='protos.BidirectionalRnn.fw_bw_rnn_cell', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rnn_regularizer', full_name='protos.BidirectionalRnn.rnn_regularizer', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_output_units', full_name='protos.BidirectionalRnn.num_output_units', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fc_hyperparams', full_name='protos.BidirectionalRnn.fc_hyperparams', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='summarize_activations', full_name='protos.BidirectionalRnn.summarize_activations', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  serialized_start=92,
  serialized_end=331,
)

_BIDIRECTIONALRNN.fields_by_name['fw_bw_rnn_cell'].message_type = protos_dot_rnn__cell__pb2._RNNCELL
_BIDIRECTIONALRNN.fields_by_name['rnn_regularizer'].message_type = protos_dot_hyperparams__pb2._REGULARIZER
_BIDIRECTIONALRNN.fields_by_name['fc_hyperparams'].message_type = protos_dot_hyperparams__pb2._HYPERPARAMS
DESCRIPTOR.message_types_by_name['BidirectionalRnn'] = _BIDIRECTIONALRNN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BidirectionalRnn = _reflection.GeneratedProtocolMessageType('BidirectionalRnn', (_message.Message,), {
  'DESCRIPTOR' : _BIDIRECTIONALRNN,
  '__module__' : 'protos.bidirectional_rnn_pb2'
  # @@protoc_insertion_point(class_scope:protos.BidirectionalRnn)
  })
_sym_db.RegisterMessage(BidirectionalRnn)


# @@protoc_insertion_point(module_scope)