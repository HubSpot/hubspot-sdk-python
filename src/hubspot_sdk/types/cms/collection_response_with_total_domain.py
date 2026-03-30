# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .domain import Domain
from ..._models import BaseModel
from ..shared.paging import Paging

__all__ = ["CollectionResponseWithTotalDomain"]


class CollectionResponseWithTotalDomain(BaseModel):
    results: List[Domain]
    """The results of the query."""

    total: int
    """The number of available results."""

    paging: Optional[Paging] = None
