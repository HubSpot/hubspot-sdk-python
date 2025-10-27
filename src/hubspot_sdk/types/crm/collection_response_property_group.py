# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .property_group import PropertyGroup
from ..marketing.paging import Paging

__all__ = ["CollectionResponsePropertyGroup"]


class CollectionResponsePropertyGroup(BaseModel):
    results: List[PropertyGroup]

    paging: Optional[Paging] = None
    """Contains information pagination of results."""
