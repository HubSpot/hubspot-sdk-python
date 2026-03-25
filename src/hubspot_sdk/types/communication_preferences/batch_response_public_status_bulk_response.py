# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.standard_error import StandardError
from .public_status_bulk_response import PublicStatusBulkResponse

__all__ = ["BatchResponsePublicStatusBulkResponse"]


class BatchResponsePublicStatusBulkResponse(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """The date and time when the batch process was completed."""

    results: List[PublicStatusBulkResponse]
    """
    The array of results from the batch process, each containing subscription status
    information.
    """

    started_at: datetime = FieldInfo(alias="startedAt")
    """The date and time when the batch process began."""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """
    The current status of the batch process, with possible values: PENDING,
    PROCESSING, CANCELED, COMPLETE.
    """

    errors: Optional[List[StandardError]] = None
    """
    An array of errors encountered during the batch operation, each represented by a
    StandardError object.
    """

    links: Optional[Dict[str, str]] = None
    """A collection of related links associated with the batch response."""

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)
    """
    The number of errors encountered during the batch operation, represented as an
    integer.
    """

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """The date and time when the batch request was made."""
