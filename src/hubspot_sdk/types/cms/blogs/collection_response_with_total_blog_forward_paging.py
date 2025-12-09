# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .blog import Blog
from ...._models import BaseModel
from ...shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponseWithTotalBlogForwardPaging"]


class CollectionResponseWithTotalBlogForwardPaging(BaseModel):
    """Response object for collections of blogs with pagination information."""

    results: List[Blog]
    """Collection of blogs."""

    total: int
    """Total number of blogs."""

    paging: Optional[ForwardPaging] = None
