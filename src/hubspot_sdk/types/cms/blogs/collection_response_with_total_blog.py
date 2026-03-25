# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .blog import Blog
from ...._models import BaseModel
from ...shared.paging import Paging

__all__ = ["CollectionResponseWithTotalBlog"]


class CollectionResponseWithTotalBlog(BaseModel):
    results: List[Blog]

    total: int

    paging: Optional[Paging] = None
