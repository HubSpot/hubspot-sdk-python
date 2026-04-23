# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .subscription_response_1 import SubscriptionResponse1

__all__ = ["CollectionResponseSubscriptionResponseNoPaging"]


class CollectionResponseSubscriptionResponseNoPaging(BaseModel):
    results: List[SubscriptionResponse1]
    """
    An array of SubscriptionResponse objects, each representing a subscription's
    details such as actions, appId, createdAt, and other relevant properties.
    """
