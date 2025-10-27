# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..marketing.paging import Paging
from .simple_public_object import SimplePublicObject

__all__ = ["CollectionResponseWithTotalSimplePublicObject"]


class CollectionResponseWithTotalSimplePublicObject(BaseModel):
    results: List[SimplePublicObject]

    total: int
    """The number of available results"""

    paging: Optional[Paging] = None
    """Contains information pagination of results."""
