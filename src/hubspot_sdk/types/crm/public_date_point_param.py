# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicDatePointParam"]


class PublicDatePointParam(TypedDict, total=False):
    day: Required[int]
    """The day component of the date."""

    month: Required[int]
    """The month component of the date."""

    time_type: Required[Annotated[Literal["DATE"], PropertyInfo(alias="timeType")]]
    """Specifies the type of time (DATE)."""

    year: Required[int]
    """The year component of the date."""

    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]
    """The identifier for the time zone."""

    hour: int
    """The hour component of the time."""

    millisecond: int
    """The millisecond component of the time."""

    minute: int
    """The minute component of the time."""

    second: int
    """The second component of the time."""

    timezone_source: Annotated[str, PropertyInfo(alias="timezoneSource")]
    """The source of the time zone information."""
