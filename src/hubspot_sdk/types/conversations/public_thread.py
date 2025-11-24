# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_thread_associations import PublicThreadAssociations

__all__ = ["PublicThread"]


class PublicThread(BaseModel):
    id: str

    archived: bool

    associated_contact_id: str = FieldInfo(alias="associatedContactId")

    created_at: datetime = FieldInfo(alias="createdAt")

    inbox_id: str = FieldInfo(alias="inboxId")

    original_channel_account_id: str = FieldInfo(alias="originalChannelAccountId")

    original_channel_id: str = FieldInfo(alias="originalChannelId")

    spam: bool

    status: Literal["CLOSED", "OPEN"]

    assigned_to: Optional[str] = FieldInfo(alias="assignedTo", default=None)

    closed_at: Optional[datetime] = FieldInfo(alias="closedAt", default=None)

    latest_message_received_timestamp: Optional[datetime] = FieldInfo(
        alias="latestMessageReceivedTimestamp", default=None
    )

    latest_message_sent_timestamp: Optional[datetime] = FieldInfo(alias="latestMessageSentTimestamp", default=None)

    latest_message_timestamp: Optional[datetime] = FieldInfo(alias="latestMessageTimestamp", default=None)

    thread_associations: Optional[PublicThreadAssociations] = FieldInfo(alias="threadAssociations", default=None)
