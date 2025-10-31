# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo
from ..quick_reply_param import QuickReplyParam
from ..contact_profile_param import ContactProfileParam
from ..social_metadata_param import SocialMetadataParam
from ..public_delivery_identifier_param import PublicDeliveryIdentifierParam

__all__ = [
    "MessageCreateParams",
    "Attachment",
    "AttachmentConversationsCustomchannelsFileAttachment",
    "AttachmentConversationsCustomchannelsLocationAttachment",
    "AttachmentConversationsCustomchannelsContactAttachment",
    "AttachmentConversationsCustomchannelsUnsupportedContentAttachment",
    "AttachmentConversationsCustomchannelsMessageHeaderAttachment",
    "AttachmentConversationsCustomchannelsQuickRepliesAttachment",
    "AttachmentConversationsCustomchannelsSocialMetadataIntegrationAttachment",
    "Recipient",
    "Sender",
    "PreResolvedContacts",
    "PreResolvedContactsContact",
]


class MessageCreateParams(TypedDict, total=False):
    attachments: Required[Iterable[Attachment]]

    channel_account_id: Required[Annotated[str, PropertyInfo(alias="channelAccountId")]]

    integration_thread_id: Required[Annotated[str, PropertyInfo(alias="integrationThreadId")]]

    message_direction: Required[Annotated[Literal["INCOMING", "OUTGOING"], PropertyInfo(alias="messageDirection")]]

    recipients: Required[Iterable[Recipient]]

    senders: Required[Iterable[Sender]]

    text: Required[str]

    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    in_reply_to_id: Annotated[str, PropertyInfo(alias="inReplyToId")]

    integration_idempotency_id: Annotated[str, PropertyInfo(alias="integrationIdempotencyId")]

    pre_resolved_contacts: Annotated[PreResolvedContacts, PropertyInfo(alias="preResolvedContacts")]

    rich_text: Annotated[str, PropertyInfo(alias="richText")]


class AttachmentConversationsCustomchannelsFileAttachment(TypedDict, total=False):
    file_id: Required[Annotated[str, PropertyInfo(alias="fileId")]]

    type: Required[Literal["FILE"]]

    file_usage_type: Annotated[str, PropertyInfo(alias="fileUsageType")]


class AttachmentConversationsCustomchannelsLocationAttachment(TypedDict, total=False):
    latitude: Required[float]

    longitude: Required[float]

    type: Required[Literal["LOCATION"]]

    address: str

    name: str

    url: str


class AttachmentConversationsCustomchannelsContactAttachment(TypedDict, total=False):
    contact_profile: Required[Annotated[ContactProfileParam, PropertyInfo(alias="contactProfile")]]

    type: Required[Literal["CONTACT"]]


class AttachmentConversationsCustomchannelsUnsupportedContentAttachment(TypedDict, total=False):
    type: Required[Literal["UNSUPPORTED_CONTENT"]]


class AttachmentConversationsCustomchannelsMessageHeaderAttachment(TypedDict, total=False):
    type: Required[Literal["MESSAGE_HEADER"]]

    file_id: Annotated[int, PropertyInfo(alias="fileId")]

    text: str


class AttachmentConversationsCustomchannelsQuickRepliesAttachment(TypedDict, total=False):
    quick_replies: Required[Annotated[Iterable[QuickReplyParam], PropertyInfo(alias="quickReplies")]]

    type: Required[Literal["QUICK_REPLIES"]]


class AttachmentConversationsCustomchannelsSocialMetadataIntegrationAttachment(TypedDict, total=False):
    social_metadata: Required[Annotated[SocialMetadataParam, PropertyInfo(alias="socialMetadata")]]

    type: Required[Literal["SOCIAL_MEDIA_METADATA"]]


Attachment: TypeAlias = Union[
    AttachmentConversationsCustomchannelsFileAttachment,
    AttachmentConversationsCustomchannelsLocationAttachment,
    AttachmentConversationsCustomchannelsContactAttachment,
    AttachmentConversationsCustomchannelsUnsupportedContentAttachment,
    AttachmentConversationsCustomchannelsMessageHeaderAttachment,
    AttachmentConversationsCustomchannelsQuickRepliesAttachment,
    AttachmentConversationsCustomchannelsSocialMetadataIntegrationAttachment,
]


class Recipient(TypedDict, total=False):
    delivery_identifier: Required[Annotated[PublicDeliveryIdentifierParam, PropertyInfo(alias="deliveryIdentifier")]]

    name: str


class Sender(TypedDict, total=False):
    delivery_identifier: Required[Annotated[PublicDeliveryIdentifierParam, PropertyInfo(alias="deliveryIdentifier")]]

    name: str


class PreResolvedContactsContact(TypedDict, total=False):
    contact_properties_leading_to_match: Required[
        Annotated[SequenceNotStr[str], PropertyInfo(alias="contactPropertiesLeadingToMatch")]
    ]

    contact_vid: Required[Annotated[int, PropertyInfo(alias="contactVid")]]


class PreResolvedContacts(TypedDict, total=False):
    contacts: Required[Iterable[PreResolvedContactsContact]]
