# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .public_inbox import PublicInbox
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponseWithTotalPublicInboxForwardPaging"]


class CollectionResponseWithTotalPublicInboxForwardPaging(BaseModel):
    results: List[PublicInbox]

    total: int

    paging: Optional[ForwardPaging] = None
