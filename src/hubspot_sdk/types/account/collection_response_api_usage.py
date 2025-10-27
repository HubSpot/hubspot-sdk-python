# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .api_usage import APIUsage
from ..marketing.paging import Paging

__all__ = ["CollectionResponseAPIUsage"]


class CollectionResponseAPIUsage(BaseModel):
    results: List[APIUsage]

    paging: Optional[Paging] = None
    """Contains information pagination of results."""
