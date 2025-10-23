# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .public_time_offset import PublicTimeOffset

__all__ = ["PublicRelativeComparativeTimestampRefineBy"]


class PublicRelativeComparativeTimestampRefineBy(TypedDict, total=False):
    comparison: Required[str]

    time_offset: Required[Annotated[PublicTimeOffset, PropertyInfo(alias="timeOffset")]]

    type: Required[Literal["RELATIVE_COMPARATIVE"]]
