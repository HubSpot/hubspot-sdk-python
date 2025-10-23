# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo
from ..file_attachment_param import FileAttachmentParam
from ..contact_attachment_param import ContactAttachmentParam
from ..location_attachment_param import LocationAttachmentParam
from ..pre_resolved_contacts_param import PreResolvedContactsParam
from ..quick_replies_attachment_param import QuickRepliesAttachmentParam
from ..message_header_attachment_param import MessageHeaderAttachmentParam
from ..unsupported_content_attachment_param import UnsupportedContentAttachmentParam
from ..channel_integration_participant_param import ChannelIntegrationParticipantParam
from ..social_metadata_integration_attachment_param import SocialMetadataIntegrationAttachmentParam

__all__ = ["MessageCreateParams", "Attachment"]


class MessageCreateParams(TypedDict, total=False):
    attachments: Required[Iterable[Attachment]]

    channel_account_id: Required[Annotated[str, PropertyInfo(alias="channelAccountId")]]

    integration_thread_id: Required[Annotated[str, PropertyInfo(alias="integrationThreadId")]]

    message_direction: Required[Annotated[Literal["INCOMING", "OUTGOING"], PropertyInfo(alias="messageDirection")]]

    recipients: Required[Iterable[ChannelIntegrationParticipantParam]]

    senders: Required[Iterable[ChannelIntegrationParticipantParam]]

    text: Required[str]

    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    in_reply_to_id: Annotated[str, PropertyInfo(alias="inReplyToId")]

    integration_idempotency_id: Annotated[str, PropertyInfo(alias="integrationIdempotencyId")]

    pre_resolved_contacts: Annotated[PreResolvedContactsParam, PropertyInfo(alias="preResolvedContacts")]

    rich_text: Annotated[str, PropertyInfo(alias="richText")]


Attachment: TypeAlias = Union[
    FileAttachmentParam,
    LocationAttachmentParam,
    ContactAttachmentParam,
    UnsupportedContentAttachmentParam,
    MessageHeaderAttachmentParam,
    QuickRepliesAttachmentParam,
    SocialMetadataIntegrationAttachmentParam,
]
