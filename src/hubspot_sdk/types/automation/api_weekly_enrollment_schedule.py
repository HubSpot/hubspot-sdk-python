# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .api_time_of_day import APITimeOfDay

__all__ = ["APIWeeklyEnrollmentSchedule"]


class APIWeeklyEnrollmentSchedule(BaseModel):
    days_of_week: List[Literal["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]] = (
        FieldInfo(alias="daysOfWeek")
    )
    """Which days of the week to allow enrollments."""

    time_of_day: APITimeOfDay = FieldInfo(alias="timeOfDay")

    type: Literal["WEEKLY"]
    """
    The type of enrollment schedule this is, can be: "DAILY", "WEEKLY",
    "MONTHLY_SPECIFIC_DAYS", "MONTHLY_RELATIVE_DAYS", "YEARLY"
    """
