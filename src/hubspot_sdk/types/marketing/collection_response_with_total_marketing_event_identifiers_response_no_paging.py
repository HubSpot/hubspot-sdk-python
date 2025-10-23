# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .marketing_event_identifiers_response import MarketingEventIdentifiersResponse

__all__ = ["CollectionResponseWithTotalMarketingEventIdentifiersResponseNoPaging"]


class CollectionResponseWithTotalMarketingEventIdentifiersResponseNoPaging(BaseModel):
    results: List[MarketingEventIdentifiersResponse]

    total: int
