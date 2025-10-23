# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIStaticTimeZoneStrategyParam"]


class APIStaticTimeZoneStrategyParam(TypedDict, total=False):
    time_zone_id: Required[Annotated[str, PropertyInfo(alias="timeZoneId")]]

    type: Required[Literal["STATIC_TIME_ZONE"]]
