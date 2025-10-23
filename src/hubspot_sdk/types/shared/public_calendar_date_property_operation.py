# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicCalendarDatePropertyOperation"]


class PublicCalendarDatePropertyOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    operation_type: Literal["CALENDAR_DATE"] = FieldInfo(alias="operationType")

    operator: str

    time_unit: str = FieldInfo(alias="timeUnit")

    fiscal_year_start: Optional[
        Literal[
            "JANUARY",
            "FEBRUARY",
            "MARCH",
            "APRIL",
            "MAY",
            "JUNE",
            "JULY",
            "AUGUST",
            "SEPTEMBER",
            "OCTOBER",
            "NOVEMBER",
            "DECEMBER",
        ]
    ] = FieldInfo(alias="fiscalYearStart", default=None)

    time_unit_count: Optional[int] = FieldInfo(alias="timeUnitCount", default=None)

    use_fiscal_year: Optional[bool] = FieldInfo(alias="useFiscalYear", default=None)
