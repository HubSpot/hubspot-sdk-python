# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .public_user import PublicUser
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponsePublicUserForwardPaging"]


class CollectionResponsePublicUserForwardPaging(BaseModel):
    results: List[PublicUser]

    paging: Optional[ForwardPaging] = None
