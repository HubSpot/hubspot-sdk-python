# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .api_time_of_day_param import APITimeOfDayParam

__all__ = ["APIYearlyEnrollmentScheduleParam"]


class APIYearlyEnrollmentScheduleParam(TypedDict, total=False):
    day_of_month: Required[Annotated[int, PropertyInfo(alias="dayOfMonth")]]

    month: Required[
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
    ]

    time_of_day: Required[Annotated[APITimeOfDayParam, PropertyInfo(alias="timeOfDay")]]

    type: Required[Literal["YEARLY"]]
