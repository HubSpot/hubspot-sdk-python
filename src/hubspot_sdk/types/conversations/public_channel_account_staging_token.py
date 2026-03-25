# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_delivery_identifier import PublicDeliveryIdentifier

__all__ = ["PublicChannelAccountStagingToken"]


class PublicChannelAccountStagingToken(BaseModel):
    account_token: str = FieldInfo(alias="accountToken")

    created_at: datetime = FieldInfo(alias="createdAt")

    generic_channel_id: int = FieldInfo(alias="genericChannelId")

    inbox_id: int = FieldInfo(alias="inboxId")

    user_id: int = FieldInfo(alias="userId")

    account_name: Optional[str] = FieldInfo(alias="accountName", default=None)

    delivery_identifier: Optional[PublicDeliveryIdentifier] = FieldInfo(alias="deliveryIdentifier", default=None)
