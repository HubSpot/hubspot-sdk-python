# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging
from .public_channel_account import PublicChannelAccount

__all__ = ["CollectionResponseWithTotalPublicChannelAccountForwardPaging"]


class CollectionResponseWithTotalPublicChannelAccountForwardPaging(BaseModel):
    results: List[PublicChannelAccount]

    total: int

    paging: Optional[ForwardPaging] = None
