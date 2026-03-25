# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .version_blog import VersionBlog
from ...shared.paging import Paging

__all__ = ["CollectionResponseWithTotalBlogVersion"]


class CollectionResponseWithTotalBlogVersion(BaseModel):
    results: List[VersionBlog]

    total: int

    paging: Optional[Paging] = None
