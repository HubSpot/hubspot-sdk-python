# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .paging import Paging
from ..._models import BaseModel
from .version_public_email import VersionPublicEmail

__all__ = ["CollectionResponseWithTotalVersionPublicEmail"]


class CollectionResponseWithTotalVersionPublicEmail(BaseModel):
    results: List[VersionPublicEmail]
    """Collection of emails."""

    total: int
    """Total number of emails."""

    paging: Optional[Paging] = None
    """Contains information pagination of results."""
