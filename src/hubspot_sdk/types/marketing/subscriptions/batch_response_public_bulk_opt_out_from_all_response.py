# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...shared.standard_error import StandardError
from .public_bulk_opt_out_from_all_response import PublicBulkOptOutFromAllResponse

__all__ = ["BatchResponsePublicBulkOptOutFromAllResponse"]


class BatchResponsePublicBulkOptOutFromAllResponse(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """The date and time when the bulk opt-out operation was completed."""

    results: List[PublicBulkOptOutFromAllResponse]
    """
    An array containing the results of the bulk opt-out from all communications
    operation.
    """

    started_at: datetime = FieldInfo(alias="startedAt")
    """The date and time when the bulk opt-out operation began."""

    status: Literal["PENDING", "PROCESSING", "CANCELED", "COMPLETE"]
    """
    The current status of the bulk opt-out operation, which can be PENDING,
    PROCESSING, CANCELED, or COMPLETE.
    """

    errors: Optional[List[StandardError]] = None
    """
    An array of error objects detailing any issues encountered during the bulk
    opt-out operation.
    """

    links: Optional[Dict[str, str]] = None
    """A collection of URLs linking to related resources or documentation."""

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)
    """The total number of errors encountered during the bulk opt-out operation."""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """The date and time when the bulk opt-out request was made."""
