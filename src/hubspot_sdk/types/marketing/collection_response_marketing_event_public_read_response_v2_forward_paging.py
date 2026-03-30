# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging
from .marketing_event_public_read_response_v2 import MarketingEventPublicReadResponseV2

__all__ = ["CollectionResponseMarketingEventPublicReadResponseV2ForwardPaging"]


class CollectionResponseMarketingEventPublicReadResponseV2ForwardPaging(BaseModel):
    results: List[MarketingEventPublicReadResponseV2]

    paging: Optional[ForwardPaging] = None
