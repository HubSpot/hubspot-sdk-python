# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .file import File
from ..._models import BaseModel
from ..shared.standard_error import StandardError

__all__ = ["FileActionResponse"]


class FileActionResponse(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """Time of completion of task."""

    started_at: datetime = FieldInfo(alias="startedAt")
    """Timestamp of when the task was started."""

    status: Literal["PENDING", "PROCESSING", "CANCELED", "COMPLETE"]
    """Current status of the task."""

    task_id: str = FieldInfo(alias="taskId")
    """ID of the requested task."""

    errors: Optional[List[StandardError]] = None
    """Descriptive error messages."""

    links: Optional[Dict[str, str]] = None
    """Link to check the status of the requested task."""

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)
    """Number of errors resulting from the task."""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """Timestamp of when the task was requested."""

    result: Optional[File] = None
    """File"""
