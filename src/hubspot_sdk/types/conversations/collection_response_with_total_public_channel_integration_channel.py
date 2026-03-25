# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from .public_channel_integration_channel import PublicChannelIntegrationChannel

__all__ = ["CollectionResponseWithTotalPublicChannelIntegrationChannel"]


class CollectionResponseWithTotalPublicChannelIntegrationChannel(BaseModel):
    results: List[PublicChannelIntegrationChannel]

    total: int

    paging: Optional[Paging] = None
