# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.property import Property
from ..marketing.paging import Paging

__all__ = ["CollectionResponseProperty"]


class CollectionResponseProperty(BaseModel):
    results: List[Property]

    paging: Optional[Paging] = None
    """Contains information pagination of results."""
