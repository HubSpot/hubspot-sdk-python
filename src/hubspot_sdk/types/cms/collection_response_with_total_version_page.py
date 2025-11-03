# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel
from ..marketing.emails_paging import EmailsPaging

__all__ = ["CollectionResponseWithTotalVersionPage"]


class CollectionResponseWithTotalVersionPage(BaseModel):
    results: List["VersionPage"]
    """Collection of page versions."""

    total: int
    """Total number of page versions."""

    paging: Optional[EmailsPaging] = None
    """Contains information pagination of results."""


from .version_page import VersionPage
