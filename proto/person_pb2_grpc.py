# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import person_pb2 as person__pb2

class ConverterCallStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.stringconverter = channel.unary_unary(
                '/ConverterCall/stringconverter',
                request_serializer=person__pb2.Person.SerializeToString,
                response_deserializer=person__pb2.Person.FromString,
                )


class ConverterCallServicer(object):
    """Missing associated documentation comment in .proto file."""

    def stringconverter(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ConverterCallServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'stringconverter': grpc.unary_unary_rpc_method_handler(
                    servicer.stringconverter,
                    request_deserializer=person__pb2.Person.FromString,
                    response_serializer=person__pb2.Person.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ConverterCall', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ConverterCall(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def stringconverter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ConverterCall/stringconverter',
            person__pb2.Person.SerializeToString,
            person__pb2.Person.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
