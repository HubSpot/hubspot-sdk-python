# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicRollingDateRangePropertyOperationParam"]


class PublicRollingDateRangePropertyOperationParam(TypedDict, total=False):
    include_objects_with_no_value_set: Required[Annotated[bool, PropertyInfo(alias="includeObjectsWithNoValueSet")]]
    """
    Indicates whether objects with no value set for the property should be included
    in the operation.
    """

    number_of_days: Required[Annotated[int, PropertyInfo(alias="numberOfDays")]]
    """The number of days to be considered in the rolling date range operation."""

    operation_type: Required[Annotated[Literal["ROLLING_DATE_RANGE"], PropertyInfo(alias="operationType")]]
    """Specifies the type of operation (ROLLING_DATE_RANGE)."""

    operator: Required[str]
    """
    Defines the operation to be applied within the rolling date range property
    operation (IS_LESS_THAN_X_DAYS_AGO, IS_MORE_THAN_X_DAYS_AGO,
    IS_LESS_THAN_X_DAYS_FROM_NOW, IS_MORE_THAN_X_DAYS_FROM_NOW).
    """

    requires_time_zone_conversion: Required[Annotated[bool, PropertyInfo(alias="requiresTimeZoneConversion")]]
    """Specifies whether the operation requires conversion to a different time zone."""
