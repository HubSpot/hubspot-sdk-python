# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicWideStatus"]


class PublicWideStatus(BaseModel):
    channel: Literal["EMAIL"]
    """The type of communication channel, with 'EMAIL' as the only supported option."""

    status: Literal["NOT_SPECIFIED", "SUBSCRIBED", "UNSUBSCRIBED"]
    """
    The subscription status of the contact, which can be 'SUBSCRIBED',
    'UNSUBSCRIBED', or 'NOT_SPECIFIED'.
    """

    subscriber_id_string: str = FieldInfo(alias="subscriberIdString")
    """The email address of the contact."""

    timestamp: datetime
    """The date and time when the status was recorded."""

    wide_status_type: Literal["BUSINESS_UNIT_WIDE", "PORTAL_WIDE"] = FieldInfo(alias="wideStatusType")
    """The type of wide status, which can be 'PORTAL_WIDE' or 'BUSINESS_UNIT_WIDE'."""

    business_unit_id: Optional[int] = FieldInfo(alias="businessUnitId", default=None)
    """The ID of the business unit associated with the status."""
