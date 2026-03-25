# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicRangedNumberPropertyOperationParam"]


class PublicRangedNumberPropertyOperationParam(TypedDict, total=False):
    include_objects_with_no_value_set: Required[Annotated[bool, PropertyInfo(alias="includeObjectsWithNoValueSet")]]
    """
    Indicates whether objects with no value set for the property should be included
    in the operation.
    """

    lower_bound: Required[Annotated[int, PropertyInfo(alias="lowerBound")]]
    """The lower limit of the number range for the operation."""

    operation_type: Required[Annotated[Literal["NUMBER_RANGED"], PropertyInfo(alias="operationType")]]
    """Specifies the type of operation (NUMBER_RANGED)."""

    operator: Required[str]
    """
    Defines the operation to be applied in the ranged number property operation
    (IS_BETWEEN, IS_NOT_BETWEEN).
    """

    upper_bound: Required[Annotated[int, PropertyInfo(alias="upperBound")]]
    """The upper limit of the number range for the operation."""
