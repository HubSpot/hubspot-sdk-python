# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.standard_error import StandardError
from .subscription_definition import SubscriptionDefinition

__all__ = ["ActionResponseWithResultsSubscriptionDefinition"]


class ActionResponseWithResultsSubscriptionDefinition(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """The date and time when the operation was completed."""

    results: List[SubscriptionDefinition]
    """An array containing the results of the operation."""

    started_at: datetime = FieldInfo(alias="startedAt")
    """The date and time when the operation started."""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """
    The current status of the operation, which can be PENDING, PROCESSING, CANCELED,
    or COMPLETE.
    """

    errors: Optional[List[StandardError]] = None
    """An array of errors that occurred during the operation."""

    links: Optional[Dict[str, str]] = None
    """A collection of related links associated with the operation."""

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)
    """The number of errors encountered during the operation."""

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """The date and time when the operation was requested."""
