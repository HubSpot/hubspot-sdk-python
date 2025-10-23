# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicAbsoluteRangedTimestampRefineBy"]


class PublicAbsoluteRangedTimestampRefineBy(TypedDict, total=False):
    lower_timestamp: Required[Annotated[int, PropertyInfo(alias="lowerTimestamp")]]

    range_type: Required[Annotated[str, PropertyInfo(alias="rangeType")]]

    type: Required[Literal["ABSOLUTE_RANGED"]]

    upper_timestamp: Required[Annotated[int, PropertyInfo(alias="upperTimestamp")]]
