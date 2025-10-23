# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging
from .public_sequence_lite_response import PublicSequenceLiteResponse

__all__ = ["CollectionResponseWithTotalPublicSequenceLiteResponseForwardPaging"]


class CollectionResponseWithTotalPublicSequenceLiteResponseForwardPaging(BaseModel):
    results: List[PublicSequenceLiteResponse]

    total: int

    paging: Optional[ForwardPaging] = None
