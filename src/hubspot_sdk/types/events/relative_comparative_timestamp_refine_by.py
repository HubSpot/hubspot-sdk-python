# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .time_offset import TimeOffset

__all__ = ["RelativeComparativeTimestampRefineBy"]


class RelativeComparativeTimestampRefineBy(BaseModel):
    comparison: Literal["BEFORE", "AFTER"]

    time_offset: TimeOffset = FieldInfo(alias="timeOffset")

    type: Literal["RelativeComparativeTimestampRefineBy"]
