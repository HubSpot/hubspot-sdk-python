# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_file import PublicFile
from .public_client import PublicClient
from .public_sender import PublicSender
from .public_contact import PublicContact
from .public_location import PublicLocation
from .public_recipient import PublicRecipient
from .public_quick_replies import PublicQuickReplies
from .public_message_header import PublicMessageHeader
from .public_message_status import PublicMessageStatus
from .public_unsupported_content import PublicUnsupportedContent
from .public_social_metadata_attachment import PublicSocialMetadataAttachment
from .public_whats_app_template_metadata import PublicWhatsAppTemplateMetadata

__all__ = ["PublicConversationsMessage", "Attachment"]

Attachment: TypeAlias = Union[
    PublicFile,
    PublicLocation,
    PublicContact,
    PublicUnsupportedContent,
    PublicMessageHeader,
    PublicQuickReplies,
    PublicWhatsAppTemplateMetadata,
    PublicSocialMetadataAttachment,
]


class PublicConversationsMessage(BaseModel):
    id: str

    archived: bool

    attachments: List[Attachment]

    channel_account_id: str = FieldInfo(alias="channelAccountId")

    channel_id: str = FieldInfo(alias="channelId")

    client: PublicClient

    conversations_thread_id: str = FieldInfo(alias="conversationsThreadId")

    created_at: datetime = FieldInfo(alias="createdAt")

    created_by: str = FieldInfo(alias="createdBy")

    direction: Literal["INCOMING", "OUTGOING"]

    recipients: List[PublicRecipient]

    senders: List[PublicSender]

    text: str

    truncation_status: Literal["NOT_TRUNCATED", "TRUNCATED_TO_MOST_RECENT_REPLY", "TRUNCATED"] = FieldInfo(
        alias="truncationStatus"
    )

    type: Literal["MESSAGE"]

    in_reply_to_id: Optional[str] = FieldInfo(alias="inReplyToId", default=None)

    rich_text: Optional[str] = FieldInfo(alias="richText", default=None)

    status: Optional[PublicMessageStatus] = None

    subject: Optional[str] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
