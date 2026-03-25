# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .exchange_rate import ExchangeRate
from ..shared.standard_error import StandardError

__all__ = ["BatchResponseExchangeRate"]


class BatchResponseExchangeRate(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")
    """The datetime the response was completed"""

    results: List[ExchangeRate]

    started_at: datetime = FieldInfo(alias="startedAt")
    """The datetime the of the request."""

    status: Literal["CANCELED", "COMPLETE", "PENDING", "PROCESSING"]
    """The current status of the response (e.g. COMPLETED)"""

    errors: Optional[List[StandardError]] = None

    links: Optional[Dict[str, str]] = None
    """The link to the next page with exchange rates."""

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
    """The datetime the of the request."""
