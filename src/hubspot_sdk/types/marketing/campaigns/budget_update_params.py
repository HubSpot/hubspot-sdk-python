# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["BudgetUpdateParams"]


class BudgetUpdateParams(TypedDict, total=False):
    campaign_guid: Required[Annotated[str, PropertyInfo(alias="campaignGuid")]]

    amount: Required[float]
    """The monetary value assigned to the budget item."""

    name: Required[str]
    """The name of the budget item."""

    order: Required[int]
    """The sequence number indicating the order of the budget item."""

    description: str
    """A detailed explanation or notes about the budget item."""
