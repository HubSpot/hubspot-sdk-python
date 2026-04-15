# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SubscriptionBatchUpdateRequestParam"]


class SubscriptionBatchUpdateRequestParam(TypedDict, total=False):
    id: Required[int]
    """The unique identifier for the subscription to be updated. It is an integer."""

    active: Required[bool]
    """A boolean indicating whether the subscription is active."""
