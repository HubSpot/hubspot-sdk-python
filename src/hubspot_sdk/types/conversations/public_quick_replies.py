# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .quick_reply import QuickReply

__all__ = ["PublicQuickReplies"]


class PublicQuickReplies(BaseModel):
    allow_multi_select: bool = FieldInfo(alias="allowMultiSelect")

    allow_user_input: bool = FieldInfo(alias="allowUserInput")

    quick_replies: List[QuickReply] = FieldInfo(alias="quickReplies")

    type: Literal["QUICK_REPLIES"]
