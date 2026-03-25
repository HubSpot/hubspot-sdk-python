# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .public_time_offset_param import PublicTimeOffsetParam

__all__ = ["PublicRelativeRangedTimestampRefineByParam"]


class PublicRelativeRangedTimestampRefineByParam(TypedDict, total=False):
    lower_bound_offset: Required[Annotated[PublicTimeOffsetParam, PropertyInfo(alias="lowerBoundOffset")]]

    range_type: Required[Annotated[str, PropertyInfo(alias="rangeType")]]
    """Specifies the type of range for the refinement criteria (BETWEEN, NOT_BETWEEN)."""

    type: Required[Literal["RELATIVE_RANGED"]]
    """Indicates the type of refinement (RELATIVE_RANGED)."""

    upper_bound_offset: Required[Annotated[PublicTimeOffsetParam, PropertyInfo(alias="upperBoundOffset")]]
