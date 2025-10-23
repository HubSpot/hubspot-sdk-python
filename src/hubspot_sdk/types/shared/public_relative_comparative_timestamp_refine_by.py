# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_time_offset import PublicTimeOffset

__all__ = ["PublicRelativeComparativeTimestampRefineBy"]


class PublicRelativeComparativeTimestampRefineBy(BaseModel):
    comparison: str

    time_offset: PublicTimeOffset = FieldInfo(alias="timeOffset")

    type: Literal["RELATIVE_COMPARATIVE"]
