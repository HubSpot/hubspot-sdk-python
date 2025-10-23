# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .quick_reply_param import QuickReplyParam

__all__ = ["QuickRepliesAttachmentParam"]


class QuickRepliesAttachmentParam(TypedDict, total=False):
    quick_replies: Required[Annotated[Iterable[QuickReplyParam], PropertyInfo(alias="quickReplies")]]

    type: Required[Literal["QUICK_REPLIES"]]
