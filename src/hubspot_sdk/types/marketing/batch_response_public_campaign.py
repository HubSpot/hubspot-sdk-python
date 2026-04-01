# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_campaign import PublicCampaign

__all__ = ["BatchResponsePublicCampaign"]


class BatchResponsePublicCampaign(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """
    The date and time when the batch operation was completed, formatted as a
    date-time string.
    """

    results: List[PublicCampaign]
    """
    An array of results from the batch operation, each item representing a public
    campaign.
    """

    started_at: datetime = FieldInfo(alias="startedAt")
    """
    The date and time when the batch operation started, formatted as a date-time
    string.
    """

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """
    The current status of the batch operation, with possible values: CANCELED,
    COMPLETE, PENDING, PROCESSING.
    """

    links: Optional[Dict[str, str]] = None
    """A map of related links associated with the batch operation."""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """
    The date and time when the batch operation was requested, formatted as a
    date-time string.
    """
