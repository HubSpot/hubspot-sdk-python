# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .blog_author import BlogAuthor
from ...shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponseWithTotalBlogAuthorForwardPaging"]


class CollectionResponseWithTotalBlogAuthorForwardPaging(BaseModel):
    results: List[BlogAuthor]
    """Collection of blog authors."""

    total: int
    """Total number of blog authors."""

    paging: Optional[ForwardPaging] = None
