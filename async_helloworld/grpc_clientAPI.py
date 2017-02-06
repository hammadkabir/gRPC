# Copyright 2015, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
from reportlab.platypus.paraparser import _num
from pip._vendor.requests.packages.urllib3._collections import _Null
from grpc._credential_composition import channel

""" Python implementation of GRPC-based client -- both insecure and SSL based."""

from grpc.beta.interfaces import ChannelConnectivity

import grpc
import time
import random
import json
import sys
import asyncio

import helloworld_echo_service_pb2
#import helloworld_echo_service_pb2_grpc

from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

_ONE_DAY_IN_SECONDS     = 60*60*24
_NUM_of_MESSAGES        = 3
_MESSAGE_SIZE           = 800


class GreeterStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SayHello = channel.unary_unary(
        '/helloworld.Greeter/SayHello',
        request_serializer=helloworld__echo__service__pb2.HelloRequest.SerializeToString,
        response_deserializer=helloworld__echo__service__pb2.HelloReply.FromString,
        )

class grpcClientAPI:
    def __init__(self, grpc_client_stub=None, msg_encoding=None):
        self.grpc_client_stub = grpc_client_stub
        self.msg_encoding = msg_encoding
        self.request_counter = 0                            # Add whatever seems fit

    def add_grpc_client(self):
        """ Adds the gRPC generated class to handled client-side gRPC operations.
        
        Returns: a gRPC client stub.
        """
        self._stub = self.grpc_client_stub(self._channel)
        return self._stub
    
    def add_grpc_client_method(self, method=None):
        """The method used by gRPC class of client to send & receive messages """
        self.client_grpc_handler = method
           
    def connect(self, ip_addr, port, callback= None):
        """
        ip_addr:    IP address of the remote peer.
        port:       Port number of the remote service.
        """
        self.ip_addr, self.port   = ip_addr, port           # IPv6 address shall be provided in square bracket.
        self.remote_addr = ip_addr + ':' + str(port)
        self._channel = grpc.insecure_channel(self.remote_addr)
        if callback is not None:
            self._channel.subscribe(callback)                # Explore the try_to_connect parameter
        
        return self._channel

    def subscribe_callback_to_channel(self, callback):
        """ The callback is executed for every change in channel connection state """
        self._channel.subscribe(callback)

    def unsubscribe_callback_to_channel(self, callback):
        """ This method removes (or unsubscribes) a callback associated to channel """
        self._channel.unsubscribe(callback)
        
    def connect_securely(self, ip_addr, port, private_key=None, certificate=None, root_certificate=None, callback=None):
        """
        ip_addr:    IP address of the remote peer.
        port:       Port number of the remote service.
        
        private_key:       Private-key of the local host
        certificate:       Certificate of the local host        # Provide this way: open('certificate_store/host.crt').read()
        root_certificate:  Root certificate that issued the client 'certificate' or any subsidary CA that issue the client certificate.
        """

        self.ip_addr, self.port   = ip_addr, port
        self.remote_addr = ip_addr + ':' + str(port)
        self.ssl_credentials = grpc.ssl_channel_credentials(root_certificates=root_certificate.encode(), private_key=private_key.encode(), certificate_chain=certificate.encode())
        self._channel = grpc.secure_channel(self.remote_addr, self.ssl_credentials)
        if callback is not None:
            self._channel.subscribe(callback)
            
        return self._channel
    

    def channel_ready(self):
        """ Returns a Future when the channel is ready to send messages 
        To this Future, one can add future.add_done_callback()
        """
        channel_ready_future = grpc.channel_ready_future(self._channel)
        return channel_ready_future
    
    def get_remote_addr(self):
        return (self.ip_addr, self.port)

    def get_grpc_handler(self):
        return self._stub

    def add_message_encoding(self, method):
        self.msg_encoding = method
        
    def message_encoding(self, msg):
        """ Returns message encoded as 'protobuf' 
        Must be sub-classed as per the RPC method in use.. For example, for sending multiple parameters instead of one.
        """
        grpc_msg = self.msg_encoding(name=msg)
        return grpc_msg
    
    def send_message(self, msg):
        """Translates message to protobuf, and sends it to the remote peer.
        Could be sub-classed as per the need.
        """
        #grpc_msg = self.message_encoding(msg)
        resp = self.client_grpc_handler(msg)
        return resp

    def send_message_async(self, msg, cb=None):
        """ Encodes the 'message' to send into protobuf, and sends it to the remote peer.
        
        Returns a future,     to which one can use add_done_callback()
        Method could be sub-classed as per the need
        """
        #grpc_msg = self.message_encoding(msg)
        response_future = self.client_grpc_handler.future(msg)
        if cb is not None:
            response_future.add_done_callback(cb)
        else:
            return response_future


    
def connection_callback(self, value):
    if value==ChannelConnectivity.IDLE:
        print("Channel is IDLE")
    elif value==ChannelConnectivity.CONNECTING:
        print("gRPC client is Connecting")
    elif value==ChannelConnectivity.READY:
        print("gRPC client is Ready to send messages")
    elif value==ChannelConnectivity.SHUTDOWN:                       # This channel SHUTDOWN status is never reported by gRPC, which is a problem.
        print("Channel closed")
    elif value==ChannelConnectivity.TRANSIENT_FAILURE:
        print("Channel is facing temporary connectivity issues")
    else:
        print(value)


def channel_ready_cb(future_ins):
    try:
        print("Channel is ready to send messages", future_ins.result())
    except Exception as msg:
        print(future_ins.exception())

def cb(future):
    """ Callback extract the result of Future, or exception received by future. """
    try:
        res = future.result()
        res = res.message
        print(res)
    except Exception as ex:
        print(future.exception())
            

def generate_random_string(self, message_size=10):
    lis=list('ascii_lowercase')
    st=''.join(random.choice(lis) for _ in range(message_size))
    return st


if __name__ == '__main__':
    ip_addr, port = 'localhost', 50061
    key = open('certificate_store/client1.key').read()
    crt = open('certificate_store/client1.crt').read()
    root_crt = open('certificate_store/CA.crt').read()      

    c = grpcClientAPI(grpc_client_stub=helloworld_echo_service_pb2.GreeterStub, msg_encoding=helloworld_echo_service_pb2.HelloRequest)
    comm_channel = c.connect(ip_addr, port)                                                    # Un-encrypted connection
    #c.connect_securely(ip_addr, port, private_key=key, certificate=crt, root_certificate=root_crt)
    channel_ready_future = grpc.channel_ready_future(comm_channel)
    #channel_ready_future.add_done_callback(channel_ready_cb)
    
    try:
        res = channel_ready_future.result(timeout=None)
        print("The channel is ready.", res)
    except Exception as msg:
        print("Exception: ", channel_ready_future.exception())
           
    client_stub = c.add_grpc_client()
    c.add_grpc_client_method(method = client_stub.SayHello)
    
    for it in range(10):                                # To send a set of messages
        msg = "I am Hammad"+str(it)
        grpc_msg = c.message_encoding(msg)
        resp = c.send_message_async(grpc_msg)           # Asynchronous message sending
        resp.add_done_callback(cb)
        #resp = c.send_message(grpc_msg)                # Synchronous/Blocking message sending
        #print(resp.message)



try:
    while True:
        time.sleep(_ONE_DAY_IN_SECONDS)
except KeyboardInterrupt:
    print('\nClient instance terminates')
