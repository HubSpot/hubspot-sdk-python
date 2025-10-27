# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .public_file_egg_param import PublicFileEggParam
from .public_recipient_egg_param import PublicRecipientEggParam
from .public_social_media_egg_param import PublicSocialMediaEggParam
from .public_quick_replies_egg_param import PublicQuickRepliesEggParam

__all__ = ["PublicConversationsMessageEggParam", "Attachment"]

Attachment: TypeAlias = Union[PublicFileEggParam, PublicQuickRepliesEggParam, PublicSocialMediaEggParam]


class PublicConversationsMessageEggParam(TypedDict, total=False):
    attachments: Required[Iterable[Attachment]]

    channel_account_id: Required[Annotated[str, PropertyInfo(alias="channelAccountId")]]

    channel_id: Required[Annotated[str, PropertyInfo(alias="channelId")]]

    recipients: Required[Iterable[PublicRecipientEggParam]]

    sender_actor_id: Required[Annotated[str, PropertyInfo(alias="senderActorId")]]

    text: Required[str]

    type: Required[Literal["MESSAGE"]]

    rich_text: Annotated[str, PropertyInfo(alias="richText")]

    subject: str
