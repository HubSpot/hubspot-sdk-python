# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .subscription_response import SubscriptionResponse

__all__ = ["BatchResponseSubscriptionResponse"]


class BatchResponseSubscriptionResponse(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """The date and time when the batch operation was completed."""

    results: List[SubscriptionResponse]
    """The list of results from the batch operation."""

    started_at: datetime = FieldInfo(alias="startedAt")
    """The date and time when the batch operation started."""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """
    The current status of the batch operation, which can be PENDING, PROCESSING,
    CANCELED, or COMPLETE.
    """

    links: Optional[Dict[str, str]] = None
    """A collection of related links associated with the batch operation."""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """The date and time when the batch operation was requested."""
