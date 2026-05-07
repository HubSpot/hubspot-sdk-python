# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponseWithTotalPageForwardPaging"]


class CollectionResponseWithTotalPageForwardPaging(BaseModel):
    results: List["PagesPage"]
    """Collection of pages."""

    total: int
    """Total number of pages."""

    paging: Optional[ForwardPaging] = None


from .pages_page import PagesPage
