# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging

__all__ = ["CollectionResponseWithTotalVersionPage"]


class CollectionResponseWithTotalVersionPage(BaseModel):
    """Response object for collections of page versions with pagination information."""

    results: List["VersionPage"]
    """Collection of page versions."""

    total: int
    """Total number of page versions."""

    paging: Optional[Paging] = None


from .version_page import VersionPage
