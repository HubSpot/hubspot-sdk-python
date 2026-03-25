# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .media_bridge_object import MediaBridgeObject
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponseMediaBridgeObjectForwardPaging"]


class CollectionResponseMediaBridgeObjectForwardPaging(BaseModel):
    results: List[MediaBridgeObject]

    paging: Optional[ForwardPaging] = None
