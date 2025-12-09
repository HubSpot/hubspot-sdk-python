# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.standard_error import StandardError
from .simple_public_upsert_object import SimplePublicUpsertObject

__all__ = ["BatchResponseSimplePublicUpsertObject"]


class BatchResponseSimplePublicUpsertObject(BaseModel):
    """
    Represents the result of a batch upsert operation, including the operation’s status, timestamps, and a list of successfully created or updated objects.
    """

    completed_at: datetime = FieldInfo(alias="completedAt")
    """The timestamp when the batch process was completed, in ISO 8601 format."""

    results: List[SimplePublicUpsertObject]

    started_at: datetime = FieldInfo(alias="startedAt")
    """The timestamp when the batch process began execution, in ISO 8601 format."""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """The status of the batch processing request.

    Can be: "PENDING", "PROCESSING", "CANCELED", or "COMPLETE".
    """

    errors: Optional[List[StandardError]] = None

    links: Optional[Dict[str, str]] = None
    """An object containing relevant links related to the batch request."""

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)
    """The number of errors"""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """The timestamp when the batch process was initiated, in ISO 8601 format."""
