# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_client import PublicClient
from .public_sender import PublicSender
from .public_recipient import PublicRecipient

__all__ = ["PublicAssignmentMessage"]


class PublicAssignmentMessage(BaseModel):
    id: str

    archived: bool

    client: PublicClient

    conversations_thread_id: str = FieldInfo(alias="conversationsThreadId")

    created_at: datetime = FieldInfo(alias="createdAt")

    created_by: str = FieldInfo(alias="createdBy")

    recipients: List[PublicRecipient]

    senders: List[PublicSender]

    type: Literal["ASSIGNMENT"]

    assigned_from: Optional[str] = FieldInfo(alias="assignedFrom", default=None)

    assigned_to: Optional[str] = FieldInfo(alias="assignedTo", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
