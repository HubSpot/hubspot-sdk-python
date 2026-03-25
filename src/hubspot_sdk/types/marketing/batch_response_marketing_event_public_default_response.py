# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.standard_error import StandardError
from .marketing_event_public_default_response import MarketingEventPublicDefaultResponse

__all__ = ["BatchResponseMarketingEventPublicDefaultResponse"]


class BatchResponseMarketingEventPublicDefaultResponse(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """Timestamp of when the request was completed."""

    results: List[MarketingEventPublicDefaultResponse]

    started_at: datetime = FieldInfo(alias="startedAt")
    """Timestamp of when the request started processing."""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """Status of the response."""

    errors: Optional[List[StandardError]] = None

    links: Optional[Dict[str, str]] = None
    """Result of the request."""

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)
    """The number of errors that occurred during the request."""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """Timestamp of when the request was sent."""
