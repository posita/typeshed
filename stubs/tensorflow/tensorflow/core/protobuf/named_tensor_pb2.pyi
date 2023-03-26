"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys
import tensorflow.core.framework.tensor_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class NamedTensorProto(google.protobuf.message.Message):
    """A pair of tensor name and tensor values."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    TENSOR_FIELD_NUMBER: builtins.int
    name: builtins.str
    """Name of the tensor."""
    @property
    def tensor(self) -> tensorflow.core.framework.tensor_pb2.TensorProto:
        """The client can populate a TensorProto using a tensorflow::Tensor`, or
        directly using the protobuf field accessors.

        The client specifies whether the returned tensor values should be
        filled tensor fields (float_val, int_val, etc.) or encoded in a
        compact form in tensor.tensor_content.
        """
    def __init__(
        self,
        *,
        name: builtins.str | None = ...,
        tensor: tensorflow.core.framework.tensor_pb2.TensorProto | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["tensor", b"tensor"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "tensor", b"tensor"]) -> None: ...

global___NamedTensorProto = NamedTensorProto