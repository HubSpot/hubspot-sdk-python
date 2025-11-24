# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.standard_error import StandardError
from .subscriber_vid_response import SubscriberVidResponse

__all__ = ["BatchResponseSubscriberVidResponse"]


class BatchResponseSubscriberVidResponse(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")

    results: List[SubscriberVidResponse]

    started_at: datetime = FieldInfo(alias="startedAt")

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]

    errors: Optional[List[StandardError]] = None

    links: Optional[Dict[str, str]] = None

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
