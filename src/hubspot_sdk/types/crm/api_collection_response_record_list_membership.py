# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from .record_list_membership import RecordListMembership

__all__ = ["APICollectionResponseRecordListMembership"]


class APICollectionResponseRecordListMembership(BaseModel):
    results: List[RecordListMembership]

    paging: Optional[Paging] = None

    total: Optional[int] = None
