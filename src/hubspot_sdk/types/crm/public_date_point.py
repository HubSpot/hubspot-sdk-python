# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicDatePoint"]


class PublicDatePoint(BaseModel):
    day: int
    """The day component of the date."""

    month: int
    """The month component of the date."""

    time_type: Literal["DATE"] = FieldInfo(alias="timeType")
    """Specifies the type of time (DATE)."""

    year: int
    """The year component of the date."""

    zone_id: str = FieldInfo(alias="zoneId")
    """The identifier for the time zone."""

    hour: Optional[int] = None
    """The hour component of the time."""

    millisecond: Optional[int] = None
    """The millisecond component of the time."""

    minute: Optional[int] = None
    """The minute component of the time."""

    second: Optional[int] = None
    """The second component of the time."""

    timezone_source: Optional[str] = FieldInfo(alias="timezoneSource", default=None)
    """The source of the time zone information."""
