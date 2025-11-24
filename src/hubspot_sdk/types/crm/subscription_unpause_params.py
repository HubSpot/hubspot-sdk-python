# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SubscriptionUnpauseParams"]


class SubscriptionUnpauseParams(TypedDict, total=False):
    proposed_next_billing_date: Required[Annotated[int, PropertyInfo(alias="proposedNextBillingDate")]]
