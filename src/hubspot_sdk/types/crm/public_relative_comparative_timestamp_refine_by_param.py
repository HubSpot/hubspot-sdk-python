# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .public_time_offset_param import PublicTimeOffsetParam

__all__ = ["PublicRelativeComparativeTimestampRefineByParam"]


class PublicRelativeComparativeTimestampRefineByParam(TypedDict, total=False):
    comparison: Required[str]
    """Defines the comparison operation to be used in the refinement (BEFORE, AFTER)."""

    time_offset: Required[Annotated[PublicTimeOffsetParam, PropertyInfo(alias="timeOffset")]]

    type: Required[Literal["RELATIVE_COMPARATIVE"]]
    """Specifies the type of refinement, (RELATIVE_COMPARATIVE)."""
