# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .property import Property
from ..._models import BaseModel

__all__ = ["BatchResponseProperty"]


class BatchResponseProperty(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")

    results: List[Property]

    started_at: datetime = FieldInfo(alias="startedAt")

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]

    links: Optional[Dict[str, str]] = None

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
