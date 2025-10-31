# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .api_time_of_day_param import APITimeOfDayParam

__all__ = ["APIWeeklyEnrollmentScheduleParam"]


class APIWeeklyEnrollmentScheduleParam(TypedDict, total=False):
    days_of_week: Required[
        Annotated[
            List[Literal["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]],
            PropertyInfo(alias="daysOfWeek"),
        ]
    ]

    time_of_day: Required[Annotated[APITimeOfDayParam, PropertyInfo(alias="timeOfDay")]]

    type: Required[Literal["WEEKLY"]]
