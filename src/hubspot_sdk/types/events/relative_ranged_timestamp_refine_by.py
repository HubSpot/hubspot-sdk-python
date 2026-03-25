# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .time_offset import TimeOffset

__all__ = ["RelativeRangedTimestampRefineBy"]


class RelativeRangedTimestampRefineBy(BaseModel):
    lower_bound_offset: TimeOffset = FieldInfo(alias="lowerBoundOffset")

    range_type: Literal["BETWEEN", "NOT_BETWEEN"] = FieldInfo(alias="rangeType")

    type: Literal["RelativeRangedTimestampRefineBy"]

    upper_bound_offset: TimeOffset = FieldInfo(alias="upperBoundOffset")
