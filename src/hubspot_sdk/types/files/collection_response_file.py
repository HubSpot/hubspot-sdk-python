# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .file import File
from ..._models import BaseModel
from ..marketing.emails_paging import EmailsPaging

__all__ = ["CollectionResponseFile"]


class CollectionResponseFile(BaseModel):
    results: List[File]

    paging: Optional[EmailsPaging] = None
    """Contains information pagination of results."""
