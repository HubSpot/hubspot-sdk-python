# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .api_flow_listing import APIFlowListing
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponseAPIFlowListingForwardPaging"]


class CollectionResponseAPIFlowListingForwardPaging(BaseModel):
    results: List[APIFlowListing]

    paging: Optional[ForwardPaging] = None
