# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .property import Property
from ..._models import BaseModel
from ..marketing.paging import Paging

__all__ = ["CollectionResponseProperty"]


class CollectionResponseProperty(BaseModel):
    results: List[Property]

    paging: Optional[Paging] = None
    """Contains information pagination of results."""
