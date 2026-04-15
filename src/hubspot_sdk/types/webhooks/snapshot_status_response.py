# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SnapshotStatusResponse"]


class SnapshotStatusResponse(BaseModel):
    id: str
    """The unique identifier for the snapshot operation, formatted as a UUID."""

    initiated_at: int = FieldInfo(alias="initiatedAt")
    """
    A Unix timestamp in milliseconds indicating when the snapshot operation was
    initiated.
    """

    status: Literal["COMPLETED", "EXPIRED", "FAILED", "IN_PROGRESS", "PENDING"]
    """The current status of the snapshot operation.

    Valid values include 'PENDING', 'IN_PROGRESS', 'COMPLETED', 'FAILED', and
    'EXPIRED'.
    """

    completed_at: Optional[int] = FieldInfo(alias="completedAt", default=None)
    """
    A Unix timestamp in milliseconds indicating when the snapshot operation was
    completed.
    """

    error_code: Optional[Literal["INTERNAL_ERROR", "PERMISSION_DENIED", "TIMEOUT", "VALIDATION_ERROR"]] = FieldInfo(
        alias="errorCode", default=None
    )
    """The code representing any error that occurred during the snapshot operation.

    Possible values are 'TIMEOUT', 'VALIDATION_ERROR', 'INTERNAL_ERROR', and
    'PERMISSION_DENIED'.
    """

    message: Optional[str] = None
    """
    A descriptive message providing additional information about the snapshot
    operation or any errors encountered.
    """
