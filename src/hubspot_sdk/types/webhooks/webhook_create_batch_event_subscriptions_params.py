# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .subscription_batch_update_request_param import SubscriptionBatchUpdateRequestParam

__all__ = ["WebhookCreateBatchEventSubscriptionsParams"]


class WebhookCreateBatchEventSubscriptionsParams(TypedDict, total=False):
    inputs: Required[Iterable[SubscriptionBatchUpdateRequestParam]]
    """
    An array of SubscriptionBatchUpdateRequest objects, each representing a
    subscription to be updated. This property is required.
    """
