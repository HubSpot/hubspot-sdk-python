# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .contact_reference import ContactReference
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponseContactReferenceForwardPaging"]


class CollectionResponseContactReferenceForwardPaging(BaseModel):
    results: List[ContactReference]
    """An array of contact references, each containing an identifier for a contact."""

    paging: Optional[ForwardPaging] = None
