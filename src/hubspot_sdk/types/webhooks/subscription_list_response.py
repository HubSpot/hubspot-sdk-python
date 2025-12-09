# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .subscription_response import SubscriptionResponse

__all__ = ["SubscriptionListResponse"]


class SubscriptionListResponse(BaseModel):
    """List of event subscriptions for your app"""

    results: List[SubscriptionResponse]
    """List of event subscriptions for your app"""
