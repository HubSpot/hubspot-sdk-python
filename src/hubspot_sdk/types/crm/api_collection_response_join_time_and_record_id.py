# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from .join_time_and_record_id import JoinTimeAndRecordID

__all__ = ["APICollectionResponseJoinTimeAndRecordID"]


class APICollectionResponseJoinTimeAndRecordID(BaseModel):
    results: List[JoinTimeAndRecordID]

    paging: Optional[Paging] = None

    total: Optional[int] = None
