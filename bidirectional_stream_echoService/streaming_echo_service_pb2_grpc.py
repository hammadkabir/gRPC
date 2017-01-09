import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import streaming_echo_service_pb2 as streaming__echo__service__pb2
import streaming_echo_service_pb2 as streaming__echo__service__pb2


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
        request_serializer=streaming__echo__service__pb2.HelloRequest.SerializeToString,
        response_deserializer=streaming__echo__service__pb2.HelloReply.FromString,
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
          request_deserializer=streaming__echo__service__pb2.HelloRequest.FromString,
          response_serializer=streaming__echo__service__pb2.HelloReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'streamingechoservice.MultiGreeter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
