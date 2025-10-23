# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .api_time_of_day import APITimeOfDay
from .api_static_time_zone_strategy import APIStaticTimeZoneStrategy

__all__ = ["APITimeDelay"]


class APITimeDelay(BaseModel):
    days_of_week: List[Literal["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]] = (
        FieldInfo(alias="daysOfWeek")
    )

    delta: int

    time_unit: Literal[
        "NANOS",
        "MICROS",
        "MILLIS",
        "SECONDS",
        "MINUTES",
        "HOURS",
        "HALF_DAYS",
        "DAYS",
        "WEEKS",
        "MONTHS",
        "YEARS",
        "DECADES",
        "CENTURIES",
        "MILLENNIA",
        "ERAS",
        "FOREVER",
    ] = FieldInfo(alias="timeUnit")

    time_of_day: Optional[APITimeOfDay] = FieldInfo(alias="timeOfDay", default=None)

    time_zone_strategy: Optional[APIStaticTimeZoneStrategy] = FieldInfo(alias="timeZoneStrategy", default=None)
