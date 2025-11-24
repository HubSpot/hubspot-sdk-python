# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .api_time_of_day import APITimeOfDay

__all__ = ["APIMonthlyRelativeDaysEnrollmentSchedule"]


class APIMonthlyRelativeDaysEnrollmentSchedule(BaseModel):
    monthly_relative_days: Literal["FIRST_MONDAY_OF_MONTH", "LAST_DAY_OF_MONTH"] = FieldInfo(
        alias="monthlyRelativeDays"
    )

    time_of_day: APITimeOfDay = FieldInfo(alias="timeOfDay")

    type: Literal["MONTHLY_RELATIVE_DAYS"]
