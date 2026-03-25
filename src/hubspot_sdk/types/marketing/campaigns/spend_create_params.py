# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SpendCreateParams"]


class SpendCreateParams(TypedDict, total=False):
    amount: Required[float]
    """The monetary value of the spend item."""

    name: Required[str]
    """The name of the spend item."""

    order: Required[int]
    """The sequence number indicating the order of the spend item."""

    description: str
    """A brief description of the spend item."""
