# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BudgetCreateParams"]


class BudgetCreateParams(TypedDict, total=False):
    amount: Required[float]
    """The monetary value assigned to the budget item."""

    name: Required[str]
    """The name of the budget item."""

    order: Required[int]
    """The sequence number indicating the order of the budget item."""

    description: str
    """A detailed explanation or notes about the budget item."""
