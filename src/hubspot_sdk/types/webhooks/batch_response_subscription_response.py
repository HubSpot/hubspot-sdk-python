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
    """The date and time when the batch operation was completed, in ISO 8601 format."""

    results: List[SubscriptionResponse]
    """
    An array containing the results of the batch operation, with each item
    representing an individual subscription response.
    """

    started_at: datetime = FieldInfo(alias="startedAt")
    """The date and time when the batch operation started, in ISO 8601 format."""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """The current status of the batch operation.

    Valid values include 'PENDING', 'PROCESSING', 'CANCELED', and 'COMPLETE'.
    """

    links: Optional[Dict[str, str]] = None
    """
    A map of link names to associated URIs providing additional information about
    the batch operation.
    """

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """The date and time when the batch operation was requested, in ISO 8601 format."""
