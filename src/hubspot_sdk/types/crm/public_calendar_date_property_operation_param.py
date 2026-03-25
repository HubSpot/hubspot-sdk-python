# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicCalendarDatePropertyOperationParam"]


class PublicCalendarDatePropertyOperationParam(TypedDict, total=False):
    include_objects_with_no_value_set: Required[Annotated[bool, PropertyInfo(alias="includeObjectsWithNoValueSet")]]
    """
    Indicates whether objects with no value set for the property should be included.
    """

    operation_type: Required[Annotated[Literal["CALENDAR_DATE"], PropertyInfo(alias="operationType")]]
    """The type of operation, which is (CALENDAR_DATE)."""

    operator: Required[str]
    """
    Defines the operation to be applied to the calendar date property
    (IN_THIS_TIME_UNIT, IN_THIS_TIME_UNIT_SO_FAR, IN_NEXT_TIME_UNIT,
    IN_LAST_TIME_UNIT).
    """

    time_unit: Required[Annotated[str, PropertyInfo(alias="timeUnit")]]
    """The unit of time to be used in the operation (DAY, WEEK, MONTH, QUARTER, YEAR)."""

    fiscal_year_start: Annotated[
        Literal[
            "APRIL",
            "AUGUST",
            "DECEMBER",
            "FEBRUARY",
            "JANUARY",
            "JULY",
            "JUNE",
            "MARCH",
            "MAY",
            "NOVEMBER",
            "OCTOBER",
            "SEPTEMBER",
        ],
        PropertyInfo(alias="fiscalYearStart"),
    ]
    """The month in which the fiscal year starts."""

    time_unit_count: Annotated[int, PropertyInfo(alias="timeUnitCount")]
    """The count of time units to be applied in the operation (1)."""

    use_fiscal_year: Annotated[bool, PropertyInfo(alias="useFiscalYear")]
    """Specifies whether the fiscal year should be used in the operation."""
