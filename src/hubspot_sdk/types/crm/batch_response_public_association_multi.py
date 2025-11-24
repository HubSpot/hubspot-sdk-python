# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.standard_error import StandardError
from .public_association_multi import PublicAssociationMulti

__all__ = ["BatchResponsePublicAssociationMulti"]


class BatchResponsePublicAssociationMulti(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """The date and time when the batch operation was completed."""

    results: List[PublicAssociationMulti]

    started_at: datetime = FieldInfo(alias="startedAt")
    """The date and time when the batch operation started."""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """
    The current status of the batch operation, with possible values: PENDING,
    PROCESSING, CANCELED, COMPLETE.
    """

    errors: Optional[List[StandardError]] = None

    links: Optional[Dict[str, str]] = None
    """URLs linking to resources or documentation associated with the batch operation."""

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)
    """The number of errors encountered during the batch operation."""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """The date and time when the batch request was made."""
