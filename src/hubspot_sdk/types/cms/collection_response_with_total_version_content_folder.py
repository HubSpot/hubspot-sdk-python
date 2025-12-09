# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from .version_content_folder import VersionContentFolder

__all__ = ["CollectionResponseWithTotalVersionContentFolder"]


class CollectionResponseWithTotalVersionContentFolder(BaseModel):
    """
    Response object for collections of content folder versions with pagination information.
    """

    results: List[VersionContentFolder]
    """Collection of content folder versions."""

    total: int
    """Total number of content folder versions."""

    paging: Optional[Paging] = None
