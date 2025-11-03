# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging
from .conversations_public_channel_account import ConversationsPublicChannelAccount

__all__ = ["CollectionResponseWithTotalPublicChannelAccountForwardPaging"]


class CollectionResponseWithTotalPublicChannelAccountForwardPaging(BaseModel):
    results: List[ConversationsPublicChannelAccount]

    total: int

    paging: Optional[ForwardPaging] = None
