# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .subscription_response import SubscriptionResponse

__all__ = ["CollectionResponseSubscriptionResponseNoPaging"]


class CollectionResponseSubscriptionResponseNoPaging(BaseModel):
    results: List[SubscriptionResponse]
    """
    An array of subscription responses, where each item contains details about a
    specific subscription. Each item follows the SubscriptionResponse schema.
    """
