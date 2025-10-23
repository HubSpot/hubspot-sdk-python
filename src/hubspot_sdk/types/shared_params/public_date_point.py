# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicDatePoint"]


class PublicDatePoint(TypedDict, total=False):
    day: Required[int]

    month: Required[int]

    time_type: Required[Annotated[Literal["DATE"], PropertyInfo(alias="timeType")]]

    year: Required[int]

    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]

    hour: int

    millisecond: int

    minute: int

    second: int

    timezone_source: Annotated[str, PropertyInfo(alias="timezoneSource")]
