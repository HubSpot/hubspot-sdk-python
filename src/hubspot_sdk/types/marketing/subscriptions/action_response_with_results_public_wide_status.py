# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .public_wide_status import PublicWideStatus
from ...shared.standard_error import StandardError

__all__ = ["ActionResponseWithResultsPublicWideStatus"]


class ActionResponseWithResultsPublicWideStatus(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """The date and time when the operation was completed."""

    results: List[PublicWideStatus]
    """An array containing the results of the operation."""

    started_at: datetime = FieldInfo(alias="startedAt")
    """The date and time when the operation started."""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """
    The current status of the operation, which can be PENDING, PROCESSING, CANCELED,
    or COMPLETE.
    """

    errors: Optional[List[StandardError]] = None
    """
    An array of error objects detailing any issues encountered during the operation.
    """

    links: Optional[Dict[str, str]] = None
    """
    An object containing related links, where each key is a link name and each value
    is a URL.
    """

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)
    """The number of errors encountered during the operation."""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """The date and time when the request was made."""
