# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .api_time_of_day import APITimeOfDay

__all__ = ["APIMonthlyRelativeDaysEnrollmentSchedule"]


class APIMonthlyRelativeDaysEnrollmentSchedule(BaseModel):
    monthly_relative_days: Literal["LAST_DAY_OF_MONTH", "FIRST_MONDAY_OF_MONTH"] = FieldInfo(
        alias="monthlyRelativeDays"
    )
    """Can be either "LAST_DAY_OF_MONTH" or "FIRST_MONDAY_OF_MONTH" """

    time_of_day: APITimeOfDay = FieldInfo(alias="timeOfDay")

    type: Literal["MONTHLY_RELATIVE_DAYS"]
    """
    The type of enrollment schedule this is, can be: "DAILY", "WEEKLY",
    "MONTHLY_SPECIFIC_DAYS", "MONTHLY_RELATIVE_DAYS", "YEARLY"
    """
