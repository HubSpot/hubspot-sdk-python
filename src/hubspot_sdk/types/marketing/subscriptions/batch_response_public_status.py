# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .public_status import PublicStatus
from ...shared.standard_error import StandardError

__all__ = ["BatchResponsePublicStatus"]


class BatchResponsePublicStatus(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """The date and time when the batch operation was completed."""

    results: List[PublicStatus]
    """An array containing the results of the batch operation."""

    started_at: datetime = FieldInfo(alias="startedAt")
    """The date and time when the batch operation started."""

    status: Literal["PENDING", "PROCESSING", "CANCELED", "COMPLETE"]
    """
    The current status of the batch operation, which can be PENDING, PROCESSING,
    CANCELED, or COMPLETE.
    """

    errors: Optional[List[StandardError]] = None
    """An array of error objects detailing any issues encountered."""

    links: Optional[Dict[str, str]] = None
    """URLs linking to related resources or documentation."""

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)
    """The number of errors encountered during the batch operation."""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """The date and time when the request was made."""
