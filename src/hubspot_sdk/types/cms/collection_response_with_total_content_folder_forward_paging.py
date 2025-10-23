# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .content_folder import ContentFolder
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponseWithTotalContentFolderForwardPaging"]


class CollectionResponseWithTotalContentFolderForwardPaging(BaseModel):
    results: List[ContentFolder]
    """Collection of content folders."""

    total: int
    """Total number of content folders."""

    paging: Optional[ForwardPaging] = None
