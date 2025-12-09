# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .version_blog import VersionBlog
from ...shared.paging import Paging

__all__ = ["CollectionResponseWithTotalVersionBlog"]


class CollectionResponseWithTotalVersionBlog(BaseModel):
    """Response object for collections of blog versions with pagination information."""

    results: List[VersionBlog]
    """Collection of blog versions."""

    total: int
    """Total number of blog versions."""

    paging: Optional[Paging] = None
