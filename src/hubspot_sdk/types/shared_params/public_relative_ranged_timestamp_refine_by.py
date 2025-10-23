# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .public_time_offset import PublicTimeOffset

__all__ = ["PublicRelativeRangedTimestampRefineBy"]


class PublicRelativeRangedTimestampRefineBy(TypedDict, total=False):
    lower_bound_offset: Required[Annotated[PublicTimeOffset, PropertyInfo(alias="lowerBoundOffset")]]

    range_type: Required[Annotated[str, PropertyInfo(alias="rangeType")]]

    type: Required[Literal["RELATIVE_RANGED"]]

    upper_bound_offset: Required[Annotated[PublicTimeOffset, PropertyInfo(alias="upperBoundOffset")]]
