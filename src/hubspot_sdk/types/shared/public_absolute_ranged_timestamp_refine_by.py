# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicAbsoluteRangedTimestampRefineBy"]


class PublicAbsoluteRangedTimestampRefineBy(BaseModel):
    lower_timestamp: int = FieldInfo(alias="lowerTimestamp")

    range_type: str = FieldInfo(alias="rangeType")

    type: Literal["ABSOLUTE_RANGED"]

    upper_timestamp: int = FieldInfo(alias="upperTimestamp")
