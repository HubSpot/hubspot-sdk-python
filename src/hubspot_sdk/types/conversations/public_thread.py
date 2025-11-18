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
    """The unique ID of the thread."""

    archived: bool
    """Whether this thread is archived."""

    associated_contact_id: str = FieldInfo(alias="associatedContactId")
    """The ID of the associated Contact in the CRM.

    If the Contact for the thread has not yet been added or created, the
    `associatedContactId` returned will be a visitorID and cannot be used to search
    for the Contact in the CRM.
    """

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the thread was created."""

    inbox_id: str = FieldInfo(alias="inboxId")
    """The ID of the conversations inbox containing the thread."""

    original_channel_account_id: str = FieldInfo(alias="originalChannelAccountId")

    original_channel_id: str = FieldInfo(alias="originalChannelId")

    spam: bool
    """Whether the thread is marked as spam."""

    status: Literal["OPEN", "CLOSED"]
    """The thread's status: `OPEN` or `CLOSED`."""

    assigned_to: Optional[str] = FieldInfo(alias="assignedTo", default=None)

    closed_at: Optional[datetime] = FieldInfo(alias="closedAt", default=None)
    """When the thread was closed. Only set if the thread is closed."""

    latest_message_received_timestamp: Optional[datetime] = FieldInfo(
        alias="latestMessageReceivedTimestamp", default=None
    )
    """The time that the latest message was sent on the thread."""

    latest_message_sent_timestamp: Optional[datetime] = FieldInfo(alias="latestMessageSentTimestamp", default=None)
    """The time that the latest message was sent on the thread."""

    latest_message_timestamp: Optional[datetime] = FieldInfo(alias="latestMessageTimestamp", default=None)
    """The time that the latest message was sent or received on the thread."""

    thread_associations: Optional[PublicThreadAssociations] = FieldInfo(alias="threadAssociations", default=None)
