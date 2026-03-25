# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_time_offset import PublicTimeOffset

__all__ = ["PublicRelativeRangedTimestampRefineBy"]


class PublicRelativeRangedTimestampRefineBy(BaseModel):
    lower_bound_offset: PublicTimeOffset = FieldInfo(alias="lowerBoundOffset")

    range_type: str = FieldInfo(alias="rangeType")
    """Specifies the type of range for the refinement criteria (BETWEEN, NOT_BETWEEN)."""

    type: Literal["RELATIVE_RANGED"]
    """Indicates the type of refinement (RELATIVE_RANGED)."""

    upper_bound_offset: PublicTimeOffset = FieldInfo(alias="upperBoundOffset")
