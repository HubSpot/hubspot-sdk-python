# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .join_time_and_record_id import JoinTimeAndRecordID
from ..marketing.emails_paging import EmailsPaging

__all__ = ["APICollectionResponseJoinTimeAndRecordID"]


class APICollectionResponseJoinTimeAndRecordID(BaseModel):
    results: List[JoinTimeAndRecordID]

    paging: Optional[EmailsPaging] = None
    """Contains information pagination of results."""

    total: Optional[int] = None
