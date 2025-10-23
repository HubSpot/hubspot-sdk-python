# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .version_blog import VersionBlog
from ...marketing.paging import Paging

__all__ = ["CollectionResponseWithTotalVersionBlog"]


class CollectionResponseWithTotalVersionBlog(BaseModel):
    results: List[VersionBlog]
    """Collection of blog versions."""

    total: int
    """Total number of blog versions."""

    paging: Optional[Paging] = None
    """Contains information pagination of results."""
