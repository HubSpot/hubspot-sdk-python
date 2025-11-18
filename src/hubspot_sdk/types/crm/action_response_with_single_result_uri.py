# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.standard_error import StandardError

__all__ = ["ActionResponseWithSingleResultUri"]


class ActionResponseWithSingleResultUri(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """The timestamp when the export was completed, in ISO 8601 format."""

    started_at: datetime = FieldInfo(alias="startedAt")
    """The timestamp when the export process started, in ISO 8601 format."""

    status: Literal["PENDING", "PROCESSING", "CANCELED", "COMPLETE"]
    """
    The current status of the export, which can be PENDING, PROCESSING, COMPLETE or
    CANCELED.
    """

    errors: Optional[List[StandardError]] = None

    links: Optional[Dict[str, str]] = None
    """A collection of related links associated with the export."""

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)
    """The number of errors encountered during the export process."""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """The timestamp when the export request was made, in ISO 8601 format."""

    result: Optional[str] = None
    """The URL of the resulting file if the export status is COMPLETE."""
