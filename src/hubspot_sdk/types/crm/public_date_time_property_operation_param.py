# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicDateTimePropertyOperationParam"]


class PublicDateTimePropertyOperationParam(TypedDict, total=False):
    include_objects_with_no_value_set: Required[Annotated[bool, PropertyInfo(alias="includeObjectsWithNoValueSet")]]
    """
    Specifies whether objects without a set value should be included in the
    operation.
    """

    operation_type: Required[Annotated[Literal["DATETIME"], PropertyInfo(alias="operationType")]]
    """The type of operation (DATETIME)."""

    operator: Required[str]
    """
    Defines the operation to be applied, such as comparison operators (IS_BEFORE,
    IS_AFTER).
    """

    requires_time_zone_conversion: Required[Annotated[bool, PropertyInfo(alias="requiresTimeZoneConversion")]]
    """Indicates whether the timestamp requires conversion to a different time zone."""

    timestamp: Required[int]
    """The specific point in time used in the operation."""
