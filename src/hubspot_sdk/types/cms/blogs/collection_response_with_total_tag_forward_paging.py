# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .tag import Tag
from ...._models import BaseModel
from ...shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponseWithTotalTagForwardPaging"]


class CollectionResponseWithTotalTagForwardPaging(BaseModel):
    """Response object for collections of blog tags with pagination information."""

    results: List[Tag]
    """Collection of blog tags."""

    total: int
    """Total number of blog tags."""

    paging: Optional[ForwardPaging] = None
