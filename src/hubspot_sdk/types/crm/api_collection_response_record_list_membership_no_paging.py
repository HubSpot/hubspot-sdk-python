# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .record_list_membership import RecordListMembership

__all__ = ["APICollectionResponseRecordListMembershipNoPaging"]


class APICollectionResponseRecordListMembershipNoPaging(BaseModel):
    results: List[RecordListMembership]

    total: Optional[int] = None
