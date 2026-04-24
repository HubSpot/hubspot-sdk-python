# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WebhookUpdateEventSubscriptionParams"]


class WebhookUpdateEventSubscriptionParams(TypedDict, total=False):
    app_id: Required[Annotated[int, PropertyInfo(alias="appId")]]

    active: bool
    """A boolean indicating whether the subscription is active.

    If true, the subscription is active; if false, it is inactive.
    """
