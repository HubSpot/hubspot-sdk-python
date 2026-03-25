# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .simple_public_object import SimplePublicObject
from ..shared.standard_error import StandardError

__all__ = ["BatchResponseSimplePublicObject"]


class BatchResponseSimplePublicObject(BaseModel):
    """A public object batch response object"""

    completed_at: datetime = FieldInfo(alias="completedAt")
    """The timestamp when the batch processing was completed, in ISO 8601 format."""

    results: List[SimplePublicObject]

    started_at: datetime = FieldInfo(alias="startedAt")
    """The timestamp when the batch processing began, in ISO 8601 format."""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """
    The status of the batch processing request: "PENDING", "PROCESSING",
    "CANCELLED", or "COMPLETE"
    """

    errors: Optional[List[StandardError]] = None

    links: Optional[Dict[str, str]] = None
    """An object containing relevant links related to the batch request."""

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)
    """The total number of errors that occurred during the batch operation."""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """The timestamp when the batch request was initially made, in ISO 8601 format."""
