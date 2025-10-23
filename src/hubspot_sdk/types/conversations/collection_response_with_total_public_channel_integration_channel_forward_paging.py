# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging
from .public_channel_integration_channel import PublicChannelIntegrationChannel

__all__ = ["CollectionResponseWithTotalPublicChannelIntegrationChannelForwardPaging"]


class CollectionResponseWithTotalPublicChannelIntegrationChannelForwardPaging(BaseModel):
    results: List[PublicChannelIntegrationChannel]

    total: int

    paging: Optional[ForwardPaging] = None
