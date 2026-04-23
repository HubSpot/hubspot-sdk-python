# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging
from .public_action_revision import PublicActionRevision

__all__ = ["CollectionResponsePublicActionRevisionForwardPaging"]


class CollectionResponsePublicActionRevisionForwardPaging(BaseModel):
    results: List[PublicActionRevision]

    paging: Optional[ForwardPaging] = None
