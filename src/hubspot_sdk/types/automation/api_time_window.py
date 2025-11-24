# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .api_time_of_day import APITimeOfDay

__all__ = ["APITimeWindow"]


class APITimeWindow(BaseModel):
    day: Literal["FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"]

    end_time: Optional[APITimeOfDay] = FieldInfo(alias="endTime", default=None)

    start_time: Optional[APITimeOfDay] = FieldInfo(alias="startTime", default=None)
