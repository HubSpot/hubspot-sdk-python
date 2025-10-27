# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .associated_id import AssociatedID
from ..shared.paging import Paging

__all__ = ["CollectionResponseAssociatedID"]


class CollectionResponseAssociatedID(BaseModel):
    results: List[AssociatedID]

    paging: Optional[Paging] = None
