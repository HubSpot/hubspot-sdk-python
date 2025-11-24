# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIUsage"]


class APIUsage(BaseModel):
    collected_at: datetime = FieldInfo(alias="collectedAt")
    """Indicates when the cache was last updated."""

    current_usage: int = FieldInfo(alias="currentUsage")
    """How many API calls an account has made for the current day."""

    fetch_status: Literal["CACHED", "FAILURE", "NOTFOUND", "SUCCESS", "TIMEOUT"] = FieldInfo(alias="fetchStatus")
    """Status of fetching the information, including if the data came from the cache."""

    name: str
    """Name of the limit type."""

    usage_limit: int = FieldInfo(alias="usageLimit")
    """Limits by which a single integration can consume the HubSpot public APIs."""

    resets_at: Optional[datetime] = FieldInfo(alias="resetsAt", default=None)
    """Time that the limit will reset."""
