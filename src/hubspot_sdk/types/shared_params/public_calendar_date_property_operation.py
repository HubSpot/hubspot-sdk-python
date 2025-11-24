# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicCalendarDatePropertyOperation"]


class PublicCalendarDatePropertyOperation(TypedDict, total=False):
    include_objects_with_no_value_set: Required[Annotated[bool, PropertyInfo(alias="includeObjectsWithNoValueSet")]]

    operation_type: Required[Annotated[Literal["CALENDAR_DATE"], PropertyInfo(alias="operationType")]]

    operator: Required[str]

    time_unit: Required[Annotated[str, PropertyInfo(alias="timeUnit")]]

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

    time_unit_count: Annotated[int, PropertyInfo(alias="timeUnitCount")]

    use_fiscal_year: Annotated[bool, PropertyInfo(alias="useFiscalYear")]
