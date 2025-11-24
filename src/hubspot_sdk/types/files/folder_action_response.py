# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .folder import Folder
from ..._models import BaseModel
from ..shared.standard_error import StandardError

__all__ = ["FolderActionResponse"]


class FolderActionResponse(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """When the requested changes have been completed."""

    started_at: datetime = FieldInfo(alias="startedAt")
    """Timestamp representing when the task was started at."""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """Current status of the task."""

    task_id: str = FieldInfo(alias="taskId")
    """ID of the task."""

    errors: Optional[List[StandardError]] = None
    """Detailed errors resulting from the task."""

    links: Optional[Dict[str, str]] = None
    """Link to check the status of the task."""

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)
    """Number of errors resulting from the requested changes."""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """Timestamp representing when the task was requested."""

    result: Optional[Folder] = None
