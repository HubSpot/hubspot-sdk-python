# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .public_owner import PublicOwner
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponsePublicOwnerForwardPaging"]


class CollectionResponsePublicOwnerForwardPaging(BaseModel):
    results: List[PublicOwner]

    paging: Optional[ForwardPaging] = None
