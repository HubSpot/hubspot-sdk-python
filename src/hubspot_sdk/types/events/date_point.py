# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DatePoint"]


class DatePoint(BaseModel):
    day: int

    month: int

    time_type: Literal["DATE"] = FieldInfo(alias="timeType")

    timezone_source: Literal["CUSTOM", "USER", "PORTAL"] = FieldInfo(alias="timezoneSource")

    year: int

    zone_id: str = FieldInfo(alias="zoneId")

    hour: Optional[int] = None

    millisecond: Optional[int] = None

    minute: Optional[int] = None

    second: Optional[int] = None
