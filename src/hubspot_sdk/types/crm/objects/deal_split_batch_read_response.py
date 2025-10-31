# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ..simple_public_object import SimplePublicObject

__all__ = ["DealSplitBatchReadResponse", "Result"]


class Result(BaseModel):
    id: str

    splits: List[SimplePublicObject]


class DealSplitBatchReadResponse(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")

    results: List[Result]

    started_at: datetime = FieldInfo(alias="startedAt")

    status: Literal["PENDING", "PROCESSING", "CANCELED", "COMPLETE"]

    links: Optional[Dict[str, str]] = None

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
