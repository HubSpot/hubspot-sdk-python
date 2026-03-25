# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .deal_to_deal_splits import DealToDealSplits
from ..shared.standard_error import StandardError

__all__ = ["BatchResponseDealToDealSplits"]


class BatchResponseDealToDealSplits(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """
    The timestamp indicating when the batch operation was completed, in date-time
    format.
    """

    results: List[DealToDealSplits]
    """
    An array of deal-to-deal split objects representing the results of the batch
    operation.
    """

    started_at: datetime = FieldInfo(alias="startedAt")
    """The timestamp indicating when the batch operation started, in date-time format."""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """
    The current status of the batch operation, with possible values: CANCELED,
    COMPLETE, PENDING, PROCESSING.
    """

    errors: Optional[List[StandardError]] = None

    links: Optional[Dict[str, str]] = None
    """
    A map of link names to associated URIs for additional resources or
    documentation.
    """

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """
    The timestamp indicating when the batch operation was requested, in date-time
    format.
    """
