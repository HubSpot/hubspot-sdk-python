# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .public_email import PublicEmail
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponseWithTotalPublicEmailForwardPaging"]


class CollectionResponseWithTotalPublicEmailForwardPaging(BaseModel):
    results: List[PublicEmail]
    """Collection of emails."""

    total: int
    """Total number of content emails."""

    paging: Optional[ForwardPaging] = None
