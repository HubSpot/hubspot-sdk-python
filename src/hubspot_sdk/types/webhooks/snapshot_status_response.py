# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SnapshotStatusResponse"]


class SnapshotStatusResponse(BaseModel):
    id: str

    initiated_at: int = FieldInfo(alias="initiatedAt")

    status: Literal["COMPLETED", "EXPIRED", "FAILED", "IN_PROGRESS", "PENDING"]

    completed_at: Optional[int] = FieldInfo(alias="completedAt", default=None)

    error_code: Optional[Literal["INTERNAL_ERROR", "PERMISSION_DENIED", "TIMEOUT", "VALIDATION_ERROR"]] = FieldInfo(
        alias="errorCode", default=None
    )

    message: Optional[str] = None
