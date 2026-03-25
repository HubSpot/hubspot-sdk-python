# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from .marketing_event_identifiers_response import MarketingEventIdentifiersResponse

__all__ = ["CollectionResponseWithTotalMarketingEventIdentifiersResponse"]


class CollectionResponseWithTotalMarketingEventIdentifiersResponse(BaseModel):
    results: List[MarketingEventIdentifiersResponse]

    total: int

    paging: Optional[Paging] = None
