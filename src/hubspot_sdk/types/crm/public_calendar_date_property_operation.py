# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicCalendarDatePropertyOperation"]


class PublicCalendarDatePropertyOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")
    """
    Indicates whether objects with no value set for the property should be included.
    """

    operation_type: Literal["CALENDAR_DATE"] = FieldInfo(alias="operationType")
    """The type of operation, which is (CALENDAR_DATE)."""

    operator: str
    """
    Defines the operation to be applied to the calendar date property
    (IN_THIS_TIME_UNIT, IN_THIS_TIME_UNIT_SO_FAR, IN_NEXT_TIME_UNIT,
    IN_LAST_TIME_UNIT).
    """

    time_unit: str = FieldInfo(alias="timeUnit")
    """The unit of time to be used in the operation (DAY, WEEK, MONTH, QUARTER, YEAR)."""

    fiscal_year_start: Optional[
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
        ]
    ] = FieldInfo(alias="fiscalYearStart", default=None)
    """The month in which the fiscal year starts."""

    time_unit_count: Optional[int] = FieldInfo(alias="timeUnitCount", default=None)
    """The count of time units to be applied in the operation (1)."""

    use_fiscal_year: Optional[bool] = FieldInfo(alias="useFiscalYear", default=None)
    """Specifies whether the fiscal year should be used in the operation."""
