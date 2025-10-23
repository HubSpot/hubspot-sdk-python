# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_delivery_identifier import PublicDeliveryIdentifier

__all__ = ["PublicChannelAccount"]


class PublicChannelAccount(BaseModel):
    id: str

    active: bool

    archived: bool

    authorized: bool

    channel_id: str = FieldInfo(alias="channelId")

    created_at: datetime = FieldInfo(alias="createdAt")

    inbox_id: str = FieldInfo(alias="inboxId")

    name: str

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)

    delivery_identifier: Optional[PublicDeliveryIdentifier] = FieldInfo(alias="deliveryIdentifier", default=None)
