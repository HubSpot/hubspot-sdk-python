# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .public_channel import PublicChannel
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponseWithTotalPublicChannelForwardPaging"]


class CollectionResponseWithTotalPublicChannelForwardPaging(BaseModel):
    results: List[PublicChannel]

    total: int

    paging: Optional[ForwardPaging] = None
