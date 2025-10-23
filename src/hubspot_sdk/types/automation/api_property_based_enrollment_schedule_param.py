# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .api_time_of_day_param import APITimeOfDayParam

__all__ = ["APIPropertyBasedEnrollmentScheduleParam"]


class APIPropertyBasedEnrollmentScheduleParam(TypedDict, total=False):
    date_property: Required[Annotated[str, PropertyInfo(alias="dateProperty")]]

    days_delta: Required[Annotated[int, PropertyInfo(alias="daysDelta")]]

    time_of_day: Required[Annotated[APITimeOfDayParam, PropertyInfo(alias="timeOfDay")]]

    type: Required[Literal["PROPERTY_BASED"]]

    yearly: Required[bool]
