# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .standard_error import StandardError
from .journal_fetch_response import JournalFetchResponse

__all__ = ["BatchResponseJournalFetchResponseWithErrors"]


class BatchResponseJournalFetchResponseWithErrors(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """The date and time when the batch process was completed, in ISO 8601 format."""

    results: List[JournalFetchResponse]
    """
    An array of journal fetch responses, each representing a result from the batch
    process.
    """

    started_at: datetime = FieldInfo(alias="startedAt")
    """The date and time when the batch process started, in ISO 8601 format."""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """The current status of the batch process.

    Valid values include 'PENDING', 'PROCESSING', 'CANCELED', and 'COMPLETE'.
    """

    errors: Optional[List[StandardError]] = None
    """
    An array of standard errors that occurred during the batch process, providing
    details about each error.
    """

    links: Optional[Dict[str, str]] = None
    """
    A map of link names to associated URIs, providing additional context or actions
    related to the batch process.
    """

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)
    """The number of errors that occurred during the batch process."""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """The date and time when the batch request was made, in ISO 8601 format."""
