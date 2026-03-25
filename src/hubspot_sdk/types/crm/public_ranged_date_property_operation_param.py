# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicRangedDatePropertyOperationParam"]


class PublicRangedDatePropertyOperationParam(TypedDict, total=False):
    include_objects_with_no_value_set: Required[Annotated[bool, PropertyInfo(alias="includeObjectsWithNoValueSet")]]
    """
    Specifies whether objects without a set value should be included in the
    operation.
    """

    lower_bound: Required[Annotated[int, PropertyInfo(alias="lowerBound")]]
    """The lower limit of the date range for the operation."""

    operation_type: Required[Annotated[Literal["RANGED_DATE"], PropertyInfo(alias="operationType")]]
    """Specifies the type of operation (RANGED_DATE)."""

    operator: Required[str]
    """
    Defines the operation to be applied in the ranged date property operation
    (IS_BETWEEN, IS_NOT_BETWEEN).
    """

    requires_time_zone_conversion: Required[Annotated[bool, PropertyInfo(alias="requiresTimeZoneConversion")]]
    """Indicates whether the operation requires conversion to a different time zone."""

    upper_bound: Required[Annotated[int, PropertyInfo(alias="upperBound")]]
    """The upper limit of the date range for the operation."""
