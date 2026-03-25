# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicNumberPropertyOperation"]


class PublicNumberPropertyOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")
    """
    Indicates whether objects with no value set for the property should be included
    in the operation.
    """

    operation_type: Literal["NUMBER"] = FieldInfo(alias="operationType")
    """Specifies the type of operation (NUMBER)."""

    operator: str
    """
    Defines the operation to be applied in the number property operation
    (IS_EQUAL_TO, IS_NOT_EQUAL_TO, IS_GREATER_THAN, IS_GREATER_THAN_OR_EQUAL_TO,
    IS_LESS_THAN, IS_LESS_THAN_OR_EQUAL_TO, HAS_EVER_BEEN_EQUAL_TO,
    HAS_NEVER_BEEN_EQUAL_TO).
    """

    value: float
    """The numeric value to be used in the operation."""
