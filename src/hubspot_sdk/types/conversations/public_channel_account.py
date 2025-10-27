# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_delivery_identifier import PublicDeliveryIdentifier

__all__ = ["PublicChannelAccount"]


class PublicChannelAccount(BaseModel):
    archived: bool

    id: Optional[str] = None
    """The ID of the channel account."""

    active: Optional[bool] = None
    """Whether the channel account is turned on."""

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)

    authorized: Optional[bool] = None

    channel_id: Optional[str] = FieldInfo(alias="channelId", default=None)
    """The ID of the channel that the channel account is an instance of."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    delivery_identifier: Optional[PublicDeliveryIdentifier] = FieldInfo(alias="deliveryIdentifier", default=None)

    inbox_id: Optional[str] = FieldInfo(alias="inboxId", default=None)
    """The ID of the conversations inbox that contains the channel account."""

    name: Optional[str] = None
    """The name of the channel account."""
