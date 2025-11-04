# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .simple_public_upsert_object import SimplePublicUpsertObject
from .associations.standard_error_1 import StandardError1

__all__ = ["BatchResponseSimplePublicUpsertObject"]


class BatchResponseSimplePublicUpsertObject(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """The timestamp when the batch process was completed, in ISO 8601 format."""

    results: List[SimplePublicUpsertObject]

    started_at: datetime = FieldInfo(alias="startedAt")
    """The timestamp when the batch process began execution, in ISO 8601 format."""

    status: Literal["PENDING", "PROCESSING", "CANCELED", "COMPLETE"]
    """The status of the batch processing request.

    Can be: "PENDING", "PROCESSING", "CANCELED", or "COMPLETE".
    """

    errors: Optional[List[StandardError1]] = None

    links: Optional[Dict[str, str]] = None
    """An object containing relevant links related to the batch request."""

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """The timestamp when the batch process was initiated, in ISO 8601 format."""
