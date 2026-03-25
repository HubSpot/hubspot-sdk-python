# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicAbsoluteRangedTimestampRefineByParam"]


class PublicAbsoluteRangedTimestampRefineByParam(TypedDict, total=False):
    lower_timestamp: Required[Annotated[int, PropertyInfo(alias="lowerTimestamp")]]
    """Lower range timestamp of refinement criteria"""

    range_type: Required[Annotated[str, PropertyInfo(alias="rangeType")]]
    """Type of range of refinement critaria (BETWEEN, NOT_BETWEEN)"""

    type: Required[Literal["ABSOLUTE_RANGED"]]
    """type of refine by criteria (ABSOLUTE_RANGED)"""

    upper_timestamp: Required[Annotated[int, PropertyInfo(alias="upperTimestamp")]]
    """Upper range timestamp of refinement criteria"""
