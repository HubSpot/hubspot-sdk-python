# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_status import PublicStatus
from ..shared.standard_error import StandardError

__all__ = ["ActionResponseWithResultsPublicStatus"]


class ActionResponseWithResultsPublicStatus(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """The date and time when the operation was completed."""

    results: List[PublicStatus]
    """An array of results from the operation."""

    started_at: datetime = FieldInfo(alias="startedAt")
    """The date and time when the operation started."""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """
    Indicates the current status of the operation, with possible values: PENDING,
    PROCESSING, CANCELED, COMPLETE.
    """

    errors: Optional[List[StandardError]] = None
    """A list of errors that occurred during the operation."""

    links: Optional[Dict[str, str]] = None
    """Contains URLs related to the response, such as documentation or resources."""

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)
    """The number of errors that occurred during the operation."""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """The date and time when the request was made."""
