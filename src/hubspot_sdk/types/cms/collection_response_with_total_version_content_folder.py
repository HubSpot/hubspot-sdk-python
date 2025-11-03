# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .version_content_folder import VersionContentFolder
from ..marketing.emails_paging import EmailsPaging

__all__ = ["CollectionResponseWithTotalVersionContentFolder"]


class CollectionResponseWithTotalVersionContentFolder(BaseModel):
    results: List[VersionContentFolder]
    """Collection of content folder versions."""

    total: int
    """Total number of content folder versions."""

    paging: Optional[EmailsPaging] = None
    """Contains information pagination of results."""
