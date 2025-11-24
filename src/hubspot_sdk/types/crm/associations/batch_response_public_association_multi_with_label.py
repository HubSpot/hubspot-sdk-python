# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...shared.standard_error import StandardError
from .public_association_multi_with_label import PublicAssociationMultiWithLabel

__all__ = ["BatchResponsePublicAssociationMultiWithLabel"]


class BatchResponsePublicAssociationMultiWithLabel(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """The timestamp when the batch processing was completed, in ISO 8601 format."""

    results: List[PublicAssociationMultiWithLabel]

    started_at: datetime = FieldInfo(alias="startedAt")
    """The timestamp when the batch processing began, in ISO 8601 format."""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """
    The status of the batch processing request: "PENDING", "PROCESSING", "CANCELED",
    or "COMPLETE".
    """

    errors: Optional[List[StandardError]] = None

    links: Optional[Dict[str, str]] = None
    """An object containing relevant links related to the batch request."""

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)
    """The number of errors encountered during the batch processing."""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """The timestamp when the batch request was initially made, in ISO 8601 format."""
