# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .api_time_of_day_param import APITimeOfDayParam
from .api_static_time_zone_strategy_param import APIStaticTimeZoneStrategyParam

__all__ = ["APITimeDelayParam"]


class APITimeDelayParam(TypedDict, total=False):
    days_of_week: Required[
        Annotated[
            List[Literal["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]],
            PropertyInfo(alias="daysOfWeek"),
        ]
    ]

    delta: Required[int]

    time_unit: Required[
        Annotated[
            Literal[
                "CENTURIES",
                "DAYS",
                "DECADES",
                "ERAS",
                "FOREVER",
                "HALF_DAYS",
                "HOURS",
                "MICROS",
                "MILLENNIA",
                "MILLIS",
                "MINUTES",
                "MONTHS",
                "NANOS",
                "SECONDS",
                "WEEKS",
                "YEARS",
            ],
            PropertyInfo(alias="timeUnit"),
        ]
    ]

    time_of_day: Annotated[APITimeOfDayParam, PropertyInfo(alias="timeOfDay")]

    time_zone_strategy: Annotated[APIStaticTimeZoneStrategyParam, PropertyInfo(alias="timeZoneStrategy")]
