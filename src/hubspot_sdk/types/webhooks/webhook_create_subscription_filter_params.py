# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.filter import Filter

__all__ = ["WebhookCreateSubscriptionFilterParams"]


class WebhookCreateSubscriptionFilterParams(TypedDict, total=False):
    filter: Required[Filter]
    """
    Defines a single condition for searching CRM objects, specifying the property to
    filter on, the operator to use (such as equals, greater than, or contains), and
    the value(s) to compare against.
    """

    subscription_id: Required[Annotated[int, PropertyInfo(alias="subscriptionId")]]
    """The unique identifier of the subscription to which the filter will be applied.

    It is an integer formatted as int64.
    """
