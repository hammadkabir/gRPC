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

"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc
import time

import helloworld_echo_service_pb2
import helloworld_echo_service_pb2_grpc

def cb(future):
    print("Client message received", future.result())
    #print(x)

def run():
    ip_addr, port = 'localhost', 50061
    addr = ip_addr + ':' + str(port)
    
    key = open('certificate_store/client1.key').read()
    crt = open('certificate_store/client1.crt').read()
    root_crt = open('certificate_store/CA.crt').read()    
    
    client_credentials = grpc.ssl_channel_credentials(root_certificates=root_crt.encode(), private_key=key.encode(), certificate_chain=crt.encode())
    channel = grpc.secure_channel(addr, client_credentials)
    stub = helloworld_echo_service_pb2_grpc.GreeterStub(channel)
    
    for it in range(0,10):
        msg = 'Test Message: '+str(it)
        print("Client sent: ", msg)
        response_future = stub.SayHello.future(helloworld_echo_service_pb2.HelloRequest(name=msg))
        response_future.add_done_callback(cb)
        time.sleep(0.03)

    time.sleep(5)



if __name__ == '__main__':
    run()
