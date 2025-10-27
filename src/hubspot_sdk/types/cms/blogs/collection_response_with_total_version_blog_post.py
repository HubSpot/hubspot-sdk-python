# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ...._models import BaseModel
from ...marketing.paging import Paging

__all__ = ["CollectionResponseWithTotalVersionBlogPost"]


class CollectionResponseWithTotalVersionBlogPost(BaseModel):
    results: List["VersionBlogPost"]
    """Collection of blog post versions."""

    total: int
    """Total number of blog post versions."""

    paging: Optional[Paging] = None
    """Contains information pagination of results."""


from .version_blog_post import VersionBlogPost
