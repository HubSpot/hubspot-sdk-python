# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .version_blog import VersionBlog
from ...marketing.emails_paging import EmailsPaging

__all__ = ["CollectionResponseWithTotalVersionBlog"]


class CollectionResponseWithTotalVersionBlog(BaseModel):
    results: List[VersionBlog]
    """Collection of blog versions."""

    total: int
    """Total number of blog versions."""

    paging: Optional[EmailsPaging] = None
    """Contains information pagination of results."""
