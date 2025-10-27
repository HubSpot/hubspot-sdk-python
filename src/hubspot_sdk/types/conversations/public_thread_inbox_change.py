# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_client import PublicClient
from .public_sender import PublicSender
from .public_recipient import PublicRecipient

__all__ = ["PublicThreadInboxChange"]


class PublicThreadInboxChange(BaseModel):
    id: str

    archived: bool

    client: PublicClient

    conversations_thread_id: str = FieldInfo(alias="conversationsThreadId")

    created_at: datetime = FieldInfo(alias="createdAt")

    created_by: str = FieldInfo(alias="createdBy")

    from_inbox_id: str = FieldInfo(alias="fromInboxId")

    recipients: List[PublicRecipient]

    senders: List[PublicSender]

    to_inbox_id: str = FieldInfo(alias="toInboxId")

    type: Literal["THREAD_INBOX_CHANGE"]

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
