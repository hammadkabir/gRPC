# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streaming_echo_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='streaming_echo_service.proto',
  package='streamingechoservice',
  syntax='proto3',
  serialized_pb=_b('\n\x1cstreaming_echo_service.proto\x12\x14streamingechoservice\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1f\n\nHelloReply\x12\x11\n\tr_message\x18\x01 \x01(\t2f\n\x0cMultiGreeter\x12V\n\x08sayHello\x12\".streamingechoservice.HelloRequest\x1a .streamingechoservice.HelloReply\"\x00(\x01\x30\x01\x42I\n%io.grpc.examples.streamingechoserviceB\x18StreamingHelloWorldProtoP\x01\xa2\x02\x03SECb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_HELLOREQUEST = _descriptor.Descriptor(
  name='HelloRequest',
  full_name='streamingechoservice.HelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='streamingechoservice.HelloRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=82,
)


_HELLOREPLY = _descriptor.Descriptor(
  name='HelloReply',
  full_name='streamingechoservice.HelloReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='r_message', full_name='streamingechoservice.HelloReply.r_message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=115,
)

DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['HelloReply'] = _HELLOREPLY

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), dict(
  DESCRIPTOR = _HELLOREQUEST,
  __module__ = 'streaming_echo_service_pb2'
  # @@protoc_insertion_point(class_scope:streamingechoservice.HelloRequest)
  ))
_sym_db.RegisterMessage(HelloRequest)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), dict(
  DESCRIPTOR = _HELLOREPLY,
  __module__ = 'streaming_echo_service_pb2'
  # @@protoc_insertion_point(class_scope:streamingechoservice.HelloReply)
  ))
_sym_db.RegisterMessage(HelloReply)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n%io.grpc.examples.streamingechoserviceB\030StreamingHelloWorldProtoP\001\242\002\003SEC'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class MultiGreeterStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.sayHello = channel.stream_stream(
          '/streamingechoservice.MultiGreeter/sayHello',
          request_serializer=HelloRequest.SerializeToString,
          response_deserializer=HelloReply.FromString,
          )


  class MultiGreeterServicer(object):
    """The greeting service definition.
    """

    def sayHello(self, request_iterator, context):
      """Sends multiple greetings
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_MultiGreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'sayHello': grpc.stream_stream_rpc_method_handler(
            servicer.sayHello,
            request_deserializer=HelloRequest.FromString,
            response_serializer=HelloReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'streamingechoservice.MultiGreeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaMultiGreeterServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """The greeting service definition.
    """
    def sayHello(self, request_iterator, context):
      """Sends multiple greetings
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaMultiGreeterStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """The greeting service definition.
    """
    def sayHello(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
      """Sends multiple greetings
      """
      raise NotImplementedError()


  def beta_create_MultiGreeter_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('streamingechoservice.MultiGreeter', 'sayHello'): HelloRequest.FromString,
    }
    response_serializers = {
      ('streamingechoservice.MultiGreeter', 'sayHello'): HelloReply.SerializeToString,
    }
    method_implementations = {
      ('streamingechoservice.MultiGreeter', 'sayHello'): face_utilities.stream_stream_inline(servicer.sayHello),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_MultiGreeter_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('streamingechoservice.MultiGreeter', 'sayHello'): HelloRequest.SerializeToString,
    }
    response_deserializers = {
      ('streamingechoservice.MultiGreeter', 'sayHello'): HelloReply.FromString,
    }
    cardinalities = {
      'sayHello': cardinality.Cardinality.STREAM_STREAM,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'streamingechoservice.MultiGreeter', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
