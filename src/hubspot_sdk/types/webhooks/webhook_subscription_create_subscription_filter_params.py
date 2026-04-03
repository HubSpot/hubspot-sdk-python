# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .filter_param import FilterParam

__all__ = ["WebhookSubscriptionCreateSubscriptionFilterParams"]


class WebhookSubscriptionCreateSubscriptionFilterParams(TypedDict, total=False):
    filter: Required[FilterParam]
    """
    Defines a single condition for searching CRM objects, specifying the property to
    filter on, the operator to use (such as equals, greater than, or contains), and
    the value(s) to compare against.
    """

    subscription_id: Required[Annotated[int, PropertyInfo(alias="subscriptionId")]]
