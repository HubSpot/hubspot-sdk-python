# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponseWithTotalPageForwardPaging"]


class CollectionResponseWithTotalPageForwardPaging(BaseModel):
    results: List["CmsPage"]
    """Collection of pages."""

    total: int
    """Total number of pages."""

    paging: Optional[ForwardPaging] = None


from .cms_page import CmsPage
