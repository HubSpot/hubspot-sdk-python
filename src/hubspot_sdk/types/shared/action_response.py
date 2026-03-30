# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ActionResponse"]


class ActionResponse(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """The timestamp indicating when the action was completed."""

    started_at: datetime = FieldInfo(alias="startedAt")
    """The timestamp indicating when the action was started."""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """
    The current status of the action, with possible values: CANCELED, COMPLETE,
    PENDING, PROCESSING.
    """

    links: Optional[Dict[str, str]] = None
    """
    A map of link names to associated URIs containing documentation about the error
    or recommended remediation steps
    """

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """The timestamp indicating when the action was requested."""
