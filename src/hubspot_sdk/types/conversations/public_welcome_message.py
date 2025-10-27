# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_client import PublicClient
from .public_sender import PublicSender
from .public_recipient import PublicRecipient

__all__ = ["PublicWelcomeMessage"]


class PublicWelcomeMessage(BaseModel):
    id: str

    archived: bool

    channel_account_id: str = FieldInfo(alias="channelAccountId")

    channel_id: str = FieldInfo(alias="channelId")

    client: PublicClient

    conversations_thread_id: str = FieldInfo(alias="conversationsThreadId")

    created_at: datetime = FieldInfo(alias="createdAt")

    created_by: str = FieldInfo(alias="createdBy")

    recipients: List[PublicRecipient]

    senders: List[PublicSender]

    text: str

    type: Literal["WELCOME_MESSAGE"]

    rich_text: Optional[str] = FieldInfo(alias="richText", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
