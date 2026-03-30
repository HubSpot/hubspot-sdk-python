# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SubscriptionBatchUpdateRequestParam"]


class SubscriptionBatchUpdateRequestParam(TypedDict, total=False):
    id: Required[int]
    """The ID of the webhook subscription to update."""

    active: Required[bool]
    """Whether to activate or pause the webhook subscription.

    If true, the subscription will send webhook notifications. If false, the
    subscription is paused and will not send notifications.
    """
