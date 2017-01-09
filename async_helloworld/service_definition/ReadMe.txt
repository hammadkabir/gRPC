Instruction to execute the service definition file.

python3 -m grpc_tools.protoc -I/path/to/service/file --python_out=. --grpc_python_out=. /path/to/service/file/service_file_name.proto

This shall produce two files, defining gRPC metadata and client/server classes.
Subequently, one can sub-class the Classes, to implement the client and server instance of service.
