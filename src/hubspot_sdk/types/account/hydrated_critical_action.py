# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["HydratedCriticalAction"]


class HydratedCriticalAction(BaseModel):
    id: str
    """The unique ID of the activity."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The time the activity took place."""

    type: str
    """The type of activity."""

    user_id: int = FieldInfo(alias="userId")
    """The user's unique ID."""

    acting_user: Optional[str] = FieldInfo(alias="actingUser", default=None)
    """Email address of the user associated with the activity."""

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)
    """The approximate country code."""

    info_url: Optional[str] = FieldInfo(alias="infoUrl", default=None)
    """A link to the URL where the action was taken in the account."""

    ip_address: Optional[str] = FieldInfo(alias="ipAddress", default=None)
    """IP address where the activity originated."""

    location: Optional[str] = None

    object_id: Optional[str] = FieldInfo(alias="objectId", default=None)
    """The ID of the affected object."""

    region_code: Optional[str] = FieldInfo(alias="regionCode", default=None)
    """The approximate region code."""
