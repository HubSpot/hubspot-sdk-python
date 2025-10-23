# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging
from .external_link_metadata import ExternalLinkMetadata

__all__ = ["CollectionResponseWithTotalExternalLinkMetadataForwardPaging"]


class CollectionResponseWithTotalExternalLinkMetadataForwardPaging(BaseModel):
    results: List[ExternalLinkMetadata]

    total: int

    paging: Optional[ForwardPaging] = None
