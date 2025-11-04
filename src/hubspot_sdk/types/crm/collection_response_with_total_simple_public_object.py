# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .simple_public_object import SimplePublicObject
from ..marketing.emails_paging import EmailsPaging

__all__ = ["CollectionResponseWithTotalSimplePublicObject"]


class CollectionResponseWithTotalSimplePublicObject(BaseModel):
    results: List[SimplePublicObject]

    total: int

    paging: Optional[EmailsPaging] = None
    """Contains information pagination of results."""
