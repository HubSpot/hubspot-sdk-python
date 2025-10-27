# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from .property_group import PropertyGroup

__all__ = ["CollectionResponsePropertyGroup"]


class CollectionResponsePropertyGroup(BaseModel):
    results: List[PropertyGroup]

    paging: Optional[Paging] = None
