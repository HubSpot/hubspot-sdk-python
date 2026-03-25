# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from .public_sequence_lite_response import PublicSequenceLiteResponse

__all__ = ["CollectionResponseWithTotalPublicSequenceLiteResponse"]


class CollectionResponseWithTotalPublicSequenceLiteResponse(BaseModel):
    results: List[PublicSequenceLiteResponse]
    """
    An array of PublicSequenceLiteResponse objects, each representing a lightweight
    version of a sequence.
    """

    total: int
    """An integer representing the total number of sequence items available."""

    paging: Optional[Paging] = None
