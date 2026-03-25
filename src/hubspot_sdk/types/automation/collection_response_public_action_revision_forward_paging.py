# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponsePublicActionRevisionForwardPaging"]


class CollectionResponsePublicActionRevisionForwardPaging(BaseModel):
    results: List["PublicActionRevision"]

    paging: Optional[ForwardPaging] = None


from .public_action_revision import PublicActionRevision
