# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicAbsoluteRangedTimestampRefineBy"]


class PublicAbsoluteRangedTimestampRefineBy(BaseModel):
    lower_timestamp: int = FieldInfo(alias="lowerTimestamp")
    """Lower range timestamp of refinement criteria"""

    range_type: str = FieldInfo(alias="rangeType")
    """Type of range of refinement critaria (BETWEEN, NOT_BETWEEN)"""

    type: Literal["ABSOLUTE_RANGED"]
    """type of refine by criteria (ABSOLUTE_RANGED)"""

    upper_timestamp: int = FieldInfo(alias="upperTimestamp")
    """Upper range timestamp of refinement criteria"""
