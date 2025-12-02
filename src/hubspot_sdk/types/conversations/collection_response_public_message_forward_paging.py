# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .public_message import PublicMessage
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponsePublicMessageForwardPaging"]


class CollectionResponsePublicMessageForwardPaging(BaseModel):
    results: List[PublicMessage]

    paging: Optional[ForwardPaging] = None
