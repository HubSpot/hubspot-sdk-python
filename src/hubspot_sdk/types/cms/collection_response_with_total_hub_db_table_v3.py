# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from .hub_db_table_v3 import HubDBTableV3

__all__ = ["CollectionResponseWithTotalHubDBTableV3"]


class CollectionResponseWithTotalHubDBTableV3(BaseModel):
    results: List[HubDBTableV3]

    total: int

    paging: Optional[Paging] = None
