# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BudgetCreateParams"]


class BudgetCreateParams(TypedDict, total=False):
    amount: Required[float]

    name: Required[str]

    order: Required[int]

    description: str
