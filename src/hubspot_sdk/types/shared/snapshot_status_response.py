# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SnapshotStatusResponse"]


class SnapshotStatusResponse(BaseModel):
    id: str
    """The unique identifier for the snapshot operation, represented as a UUID."""

    initiated_at: int = FieldInfo(alias="initiatedAt")
    """
    The timestamp indicating when the snapshot operation was initiated, represented
    as a Unix timestamp in milliseconds.
    """

    status: Literal["COMPLETED", "EXPIRED", "FAILED", "IN_PROGRESS", "PENDING"]
    """The current status of the snapshot.

    Valid values include 'PENDING', 'IN_PROGRESS', 'COMPLETED', 'FAILED', and
    'EXPIRED'.
    """

    completed_at: Optional[int] = FieldInfo(alias="completedAt", default=None)
    """
    The timestamp indicating when the snapshot operation was completed, represented
    as a Unix timestamp in milliseconds.
    """

    error_code: Optional[Literal["INTERNAL_ERROR", "PERMISSION_DENIED", "TIMEOUT", "VALIDATION_ERROR"]] = FieldInfo(
        alias="errorCode", default=None
    )
    """A code representing the error that occurred, if any.

    Possible values are 'TIMEOUT', 'VALIDATION_ERROR', 'INTERNAL_ERROR', and
    'PERMISSION_DENIED'.
    """

    message: Optional[str] = None
    """
    A descriptive message providing additional information about the snapshot
    operation or error.
    """
