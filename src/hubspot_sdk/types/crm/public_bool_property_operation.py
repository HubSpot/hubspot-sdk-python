# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicBoolPropertyOperation"]


class PublicBoolPropertyOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")
    """
    Indicates whether objects with no value set for the property should be included
    in the operation.
    """

    operation_type: Literal["BOOL"] = FieldInfo(alias="operationType")
    """Specifies the type of operation (BOOL)."""

    operator: str
    """
    Defines the operation to be applied in the boolean property operation
    (IS_EQUAL_TO, IS_NOT_EQUAL_TO, HAS_EVER_BEEN_EQUAL_TO, HAS_NEVER_BEEN_EQUAL_TO).
    """

    value: bool
    """The boolean value to be used in the operation."""
