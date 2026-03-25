# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PublicAbsoluteComparativeTimestampRefineByParam"]


class PublicAbsoluteComparativeTimestampRefineByParam(TypedDict, total=False):
    comparison: Required[str]
    """Timestamp comparison options (BEFORE, AFTER)"""

    timestamp: Required[int]
    """Timestamp to be used in refine by criteria"""

    type: Required[Literal["ABSOLUTE_COMPARATIVE"]]
    """type of refine by criteria (ABSOLUTE_COMPARATIVE)"""
