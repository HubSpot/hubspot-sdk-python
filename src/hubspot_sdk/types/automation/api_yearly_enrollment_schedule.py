# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .api_time_of_day import APITimeOfDay

__all__ = ["APIYearlyEnrollmentSchedule"]


class APIYearlyEnrollmentSchedule(BaseModel):
    day_of_month: int = FieldInfo(alias="dayOfMonth")

    month: Literal[
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

    time_of_day: APITimeOfDay = FieldInfo(alias="timeOfDay")

    type: Literal["YEARLY"]
