# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .journal_subscription_response import JournalSubscriptionResponse

__all__ = ["JournalCollectionResponseSubscriptionResponseNoPaging"]


class JournalCollectionResponseSubscriptionResponseNoPaging(BaseModel):
    results: List[JournalSubscriptionResponse]
    """
    An array of subscription responses, where each item contains details about a
    specific subscription. Each item follows the SubscriptionResponse schema.
    """
