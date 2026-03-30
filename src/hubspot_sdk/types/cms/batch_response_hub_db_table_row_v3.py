# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .hub_db_table_row_v3 import HubDBTableRowV3
from ..shared.standard_error import StandardError

__all__ = ["BatchResponseHubDBTableRowV3"]


class BatchResponseHubDBTableRowV3(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """The timestamp indicating when the batch processing was completed."""

    results: List[HubDBTableRowV3]

    started_at: datetime = FieldInfo(alias="startedAt")
    """The timestamp indicating when the batch processing began."""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """
    The current status of the batch operation, with possible values: CANCELED,
    COMPLETE, PENDING, PROCESSING.
    """

    errors: Optional[List[StandardError]] = None

    links: Optional[Dict[str, str]] = None
    """A collection of related links associated with the batch response."""

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """The timestamp indicating when the batch request was made."""
