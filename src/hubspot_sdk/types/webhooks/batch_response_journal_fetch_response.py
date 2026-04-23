# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .journal_fetch_response import JournalFetchResponse

__all__ = ["BatchResponseJournalFetchResponse"]


class BatchResponseJournalFetchResponse(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """The date and time when the batch operation was completed, in ISO 8601 format."""

    results: List[JournalFetchResponse]
    """
    An array of results from the batch operation, each represented as a
    JournalFetchResponse object.
    """

    started_at: datetime = FieldInfo(alias="startedAt")
    """The date and time when the batch operation started, in ISO 8601 format."""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """The current status of the batch operation.

    Valid values include 'PENDING', 'PROCESSING', 'CANCELED', and 'COMPLETE'.
    """

    links: Optional[Dict[str, str]] = None
    """A map of link names to associated URIs related to the batch operation."""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """The date and time when the batch operation was requested, in ISO 8601 format."""
