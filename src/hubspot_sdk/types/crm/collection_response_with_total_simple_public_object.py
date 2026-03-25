# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from .simple_public_object import SimplePublicObject

__all__ = ["CollectionResponseWithTotalSimplePublicObject"]


class CollectionResponseWithTotalSimplePublicObject(BaseModel):
    """
    Represents a list of simple objects returned from an API request, along with the total count of objects available.
    """

    results: List[SimplePublicObject]

    total: int
    """The total number of objects included into response."""

    paging: Optional[Paging] = None
