# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .api_time_of_day_param import APITimeOfDayParam

__all__ = ["APIMonthlyRelativeDaysEnrollmentScheduleParam"]


class APIMonthlyRelativeDaysEnrollmentScheduleParam(TypedDict, total=False):
    monthly_relative_days: Required[
        Annotated[Literal["LAST_DAY_OF_MONTH", "FIRST_MONDAY_OF_MONTH"], PropertyInfo(alias="monthlyRelativeDays")]
    ]
    """Can be either "LAST_DAY_OF_MONTH" or "FIRST_MONDAY_OF_MONTH" """

    time_of_day: Required[Annotated[APITimeOfDayParam, PropertyInfo(alias="timeOfDay")]]

    type: Required[Literal["MONTHLY_RELATIVE_DAYS"]]
    """
    The type of enrollment schedule this is, can be: "DAILY", "WEEKLY",
    "MONTHLY_SPECIFIC_DAYS", "MONTHLY_RELATIVE_DAYS", "YEARLY"
    """
