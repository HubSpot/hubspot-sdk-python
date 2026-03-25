# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .url_mapping import URLMapping
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponseWithTotalURLMappingForwardPaging"]


class CollectionResponseWithTotalURLMappingForwardPaging(BaseModel):
    results: List[URLMapping]
    """An array of UrlMapping objects, each representing a specific URL mapping."""

    total: int
    """The total number of URL mappings available."""

    paging: Optional[ForwardPaging] = None
