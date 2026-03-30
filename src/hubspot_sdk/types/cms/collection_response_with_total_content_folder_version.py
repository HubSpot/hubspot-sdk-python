# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from .content_folder_version import ContentFolderVersion

__all__ = ["CollectionResponseWithTotalContentFolderVersion"]


class CollectionResponseWithTotalContentFolderVersion(BaseModel):
    results: List[ContentFolderVersion]

    total: int

    paging: Optional[Paging] = None
