# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from .public_channel_account import PublicChannelAccount

__all__ = ["CollectionResponseWithTotalPublicChannelAccount"]


class CollectionResponseWithTotalPublicChannelAccount(BaseModel):
    results: List[PublicChannelAccount]

    total: int

    paging: Optional[Paging] = None
