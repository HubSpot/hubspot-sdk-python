# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CalendarDatePropertyOperation"]


class CalendarDatePropertyOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    operation_type: str = FieldInfo(alias="operationType")

    operator: Literal["IN_LAST_TIME_UNIT", "IN_NEXT_TIME_UNIT", "IN_THIS_TIME_UNIT", "IN_THIS_TIME_UNIT_SO_FAR"]

    operator_name: str = FieldInfo(alias="operatorName")

    property_type: Literal["calendar-date"] = FieldInfo(alias="propertyType")

    time_unit: Literal["DAY", "MONTH", "QUARTER", "WEEK", "YEAR"] = FieldInfo(alias="timeUnit")

    time_unit_count: int = FieldInfo(alias="timeUnitCount")

    use_fiscal_year: bool = FieldInfo(alias="useFiscalYear")

    default_value: Optional[str] = FieldInfo(alias="defaultValue", default=None)

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
