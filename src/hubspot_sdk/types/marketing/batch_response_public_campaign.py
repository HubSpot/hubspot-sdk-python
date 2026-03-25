# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_campaign import PublicCampaign
from ..shared.standard_error import StandardError

__all__ = ["BatchResponsePublicCampaign"]


class BatchResponsePublicCampaign(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """The date and time when the batch operation was completed, in ISO 8601 format."""

    results: List[PublicCampaign]
    """
    An array of results from the batch operation, each item representing a public
    campaign.
    """

    started_at: datetime = FieldInfo(alias="startedAt")
    """The date and time when the batch operation started, in ISO 8601 format."""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """The current status of the batch operation.

    Valid values include 'PENDING', 'PROCESSING', 'CANCELED', and 'COMPLETE'.
    """

    errors: Optional[List[StandardError]] = None
    """
    An array of errors that occurred during the batch operation, each item detailing
    a specific error.
    """

    links: Optional[Dict[str, str]] = None
    """A map of link names to associated URIs related to the batch operation."""

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)
    """The number of errors that occurred during the batch operation."""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """The date and time when the batch operation was requested, in ISO 8601 format."""
