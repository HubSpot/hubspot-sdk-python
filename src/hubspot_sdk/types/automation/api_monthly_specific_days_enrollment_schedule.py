# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .api_time_of_day import APITimeOfDay

__all__ = ["APIMonthlySpecificDaysEnrollmentSchedule"]


class APIMonthlySpecificDaysEnrollmentSchedule(BaseModel):
    days_of_month: List[int] = FieldInfo(alias="daysOfMonth")
    """Which days of the month to run this workflow on."""

    time_of_day: APITimeOfDay = FieldInfo(alias="timeOfDay")

    type: Literal["MONTHLY_SPECIFIC_DAYS"]
    """
    The type of enrollment schedule this is, can be: "DAILY", "WEEKLY",
    "MONTHLY_SPECIFIC_DAYS", "MONTHLY_RELATIVE_DAYS", "YEARLY"
    """
