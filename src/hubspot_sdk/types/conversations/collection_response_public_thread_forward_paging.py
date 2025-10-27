# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .public_thread import PublicThread
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponsePublicThreadForwardPaging"]


class CollectionResponsePublicThreadForwardPaging(BaseModel):
    results: List[PublicThread]

    paging: Optional[ForwardPaging] = None
