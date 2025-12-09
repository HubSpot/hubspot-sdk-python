# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicLoginAudit"]


class PublicLoginAudit(BaseModel):
    """Details about the a particular login activity for a HubSpot account."""

    id: str
    """The login activity's unique ID."""

    login_at: datetime = FieldInfo(alias="loginAt")
    """The time the login took place."""

    login_succeeded: bool = FieldInfo(alias="loginSucceeded")
    """Whether the login was successful or not."""

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)
    """The approximate country code of the login."""

    email: Optional[str] = None
    """Email address of the user associated with the login."""

    ip_address: Optional[str] = FieldInfo(alias="ipAddress", default=None)
    """IP address where the activity originated."""

    location: Optional[str] = None

    region_code: Optional[str] = FieldInfo(alias="regionCode", default=None)
    """The approximate region code of the login."""

    user_agent: Optional[str] = FieldInfo(alias="userAgent", default=None)
    """Information about the device used for logging in."""

    user_id: Optional[int] = FieldInfo(alias="userId", default=None)
    """The user's unique ID."""
