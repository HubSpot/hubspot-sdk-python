# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from ..shared.property import Property

__all__ = ["CollectionResponseProperty"]


class CollectionResponseProperty(BaseModel):
    results: List[Property]

    paging: Optional[Paging] = None
