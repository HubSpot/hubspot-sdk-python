# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .public_list import PublicList
from ..shared.paging import Paging

__all__ = ["CollectionResponseWithTotalPublicList"]


class CollectionResponseWithTotalPublicList(BaseModel):
    results: List[PublicList]

    total: int

    paging: Optional[Paging] = None
