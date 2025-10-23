# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .api_time_of_day_param import APITimeOfDayParam

__all__ = ["APITimeWindowParam"]


class APITimeWindowParam(TypedDict, total=False):
    day: Required[Literal["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]]

    end_time: Required[Annotated[APITimeOfDayParam, PropertyInfo(alias="endTime")]]

    start_time: Required[Annotated[APITimeOfDayParam, PropertyInfo(alias="startTime")]]
