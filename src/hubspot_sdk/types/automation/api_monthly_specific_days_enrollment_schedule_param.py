# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .api_time_of_day_param import APITimeOfDayParam

__all__ = ["APIMonthlySpecificDaysEnrollmentScheduleParam"]


class APIMonthlySpecificDaysEnrollmentScheduleParam(TypedDict, total=False):
    days_of_month: Required[Annotated[Iterable[int], PropertyInfo(alias="daysOfMonth")]]

    time_of_day: Required[Annotated[APITimeOfDayParam, PropertyInfo(alias="timeOfDay")]]

    type: Required[Literal["MONTHLY_SPECIFIC_DAYS"]]
