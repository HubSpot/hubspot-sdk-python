# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WebhookSubscriptionUpdateSubscriptionParams"]


class WebhookSubscriptionUpdateSubscriptionParams(TypedDict, total=False):
    app_id: Required[Annotated[int, PropertyInfo(alias="appId")]]

    active: bool
    """Whether to activate or pause the webhook subscription.

    If true, the subscription will send webhook notifications. If false, the
    subscription is paused and will not send notifications.
    """
