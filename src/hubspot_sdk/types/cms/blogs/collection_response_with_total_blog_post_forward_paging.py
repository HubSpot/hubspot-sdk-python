# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ...._models import BaseModel
from ...shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponseWithTotalBlogPostForwardPaging"]


class CollectionResponseWithTotalBlogPostForwardPaging(BaseModel):
    """Response object for collections of blog posts with pagination information."""

    results: List["BlogPost"]
    """Collection of blog posts."""

    total: int
    """Total number of blog posts."""

    paging: Optional[ForwardPaging] = None


from .blog_post import BlogPost
