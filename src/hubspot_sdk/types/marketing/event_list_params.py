# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["EventListParams"]


class EventListParams(TypedDict, total=False):
    after: str
    """The cursor indicating the position of the last retrieved item."""

    limit: int
    """The limit for response size. The default value is 10, the max number is 100"""
