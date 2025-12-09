# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .file import File
from ..._models import BaseModel
from ..shared.paging import Paging

__all__ = ["CollectionResponseFile"]


class CollectionResponseFile(BaseModel):
    """Collections of files"""

    results: List[File]

    paging: Optional[Paging] = None
