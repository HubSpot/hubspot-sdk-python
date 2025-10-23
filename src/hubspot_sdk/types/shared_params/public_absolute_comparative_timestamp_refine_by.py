# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PublicAbsoluteComparativeTimestampRefineBy"]


class PublicAbsoluteComparativeTimestampRefineBy(TypedDict, total=False):
    comparison: Required[str]

    timestamp: Required[int]

    type: Required[Literal["ABSOLUTE_COMPARATIVE"]]
