# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from .external_link_metadata import ExternalLinkMetadata

__all__ = ["CollectionResponseWithTotalExternalLinkMetadata"]


class CollectionResponseWithTotalExternalLinkMetadata(BaseModel):
    results: List[ExternalLinkMetadata]

    total: int

    paging: Optional[Paging] = None
