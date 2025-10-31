# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AbsoluteRangedTimestampRefineBy"]


class AbsoluteRangedTimestampRefineBy(BaseModel):
    lower_timestamp: int = FieldInfo(alias="lowerTimestamp")

    range_type: Literal["BETWEEN", "NOT_BETWEEN"] = FieldInfo(alias="rangeType")

    type: Literal["AbsoluteRangedTimestampRefineBy"]

    upper_timestamp: int = FieldInfo(alias="upperTimestamp")
