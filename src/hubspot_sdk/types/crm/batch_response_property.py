# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.base_property import BaseProperty

__all__ = ["BatchResponseProperty"]


class BatchResponseProperty(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """The timestamp indicating when the batch operation was completed."""

    results: List[BaseProperty]

    started_at: datetime = FieldInfo(alias="startedAt")
    """The timestamp indicating when the batch operation began processing."""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """
    The current status of the batch operation, with possible values being CANCELED,
    COMPLETE, PENDING, or PROCESSING.
    """

    links: Optional[Dict[str, str]] = None
    """
    A collection of URLs linking to documentation or resources related to the batch
    operation.
    """

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """The timestamp indicating when the batch operation was requested."""
