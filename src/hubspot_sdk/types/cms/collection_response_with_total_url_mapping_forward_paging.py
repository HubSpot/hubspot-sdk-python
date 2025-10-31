# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .url_mapping import URLMapping
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponseWithTotalURLMappingForwardPaging"]


class CollectionResponseWithTotalURLMappingForwardPaging(BaseModel):
    results: List[URLMapping]

    total: int

    paging: Optional[ForwardPaging] = None
