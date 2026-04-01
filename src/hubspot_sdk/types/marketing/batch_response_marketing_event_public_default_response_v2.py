# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .marketing_event_public_default_response_v2 import MarketingEventPublicDefaultResponseV2

__all__ = ["BatchResponseMarketingEventPublicDefaultResponseV2"]


class BatchResponseMarketingEventPublicDefaultResponseV2(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """Timestamp of when the request was processed."""

    results: List[MarketingEventPublicDefaultResponseV2]

    started_at: datetime = FieldInfo(alias="startedAt")
    """Timestamp of when the request started processing."""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """The status of the response."""

    links: Optional[Dict[str, str]] = None
    """Result object of the request."""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """Timestamp of when the request was sent."""
