# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging

__all__ = ["CollectionResponseWithTotalPageVersion"]


class CollectionResponseWithTotalPageVersion(BaseModel):
    results: List["PageVersion"]

    total: int

    paging: Optional[Paging] = None


from .page_version import PageVersion
