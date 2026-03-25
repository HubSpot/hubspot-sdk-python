# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicRangedNumberPropertyOperation"]


class PublicRangedNumberPropertyOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")
    """
    Indicates whether objects with no value set for the property should be included
    in the operation.
    """

    lower_bound: int = FieldInfo(alias="lowerBound")
    """The lower limit of the number range for the operation."""

    operation_type: Literal["NUMBER_RANGED"] = FieldInfo(alias="operationType")
    """Specifies the type of operation (NUMBER_RANGED)."""

    operator: str
    """
    Defines the operation to be applied in the ranged number property operation
    (IS_BETWEEN, IS_NOT_BETWEEN).
    """

    upper_bound: int = FieldInfo(alias="upperBound")
    """The upper limit of the number range for the operation."""
