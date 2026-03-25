# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PublicAbsoluteComparativeTimestampRefineBy"]


class PublicAbsoluteComparativeTimestampRefineBy(BaseModel):
    comparison: str
    """Timestamp comparison options (BEFORE, AFTER)"""

    timestamp: int
    """Timestamp to be used in refine by criteria"""

    type: Literal["ABSOLUTE_COMPARATIVE"]
    """type of refine by criteria (ABSOLUTE_COMPARATIVE)"""
