# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .public_wide_status_bulk_response import PublicWideStatusBulkResponse

__all__ = ["BatchResponsePublicWideStatusBulkResponse"]


class BatchResponsePublicWideStatusBulkResponse(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """The date and time when the batch process was completed."""

    results: List[PublicWideStatusBulkResponse]
    """
    The array of results from the batch process, each containing subscription status
    information.
    """

    started_at: datetime = FieldInfo(alias="startedAt")
    """The date and time when the batch process began."""

    status: Literal["PENDING", "PROCESSING", "CANCELED", "COMPLETE"]
    """
    The current status of the batch process, with possible values: PENDING,
    PROCESSING, CANCELED, COMPLETE.
    """

    links: Optional[Dict[str, str]] = None
    """A collection of related links associated with the batch response."""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """The date and time when the batch request was made."""
