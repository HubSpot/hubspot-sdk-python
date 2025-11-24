# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .deal_to_deal_splits import DealToDealSplits

__all__ = ["BatchResponseDealToDealSplits"]


class BatchResponseDealToDealSplits(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")

    results: List[DealToDealSplits]

    started_at: datetime = FieldInfo(alias="startedAt")

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]

    links: Optional[Dict[str, str]] = None

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
