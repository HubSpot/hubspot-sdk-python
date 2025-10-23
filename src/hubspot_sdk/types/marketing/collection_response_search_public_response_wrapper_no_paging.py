# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .search_public_response_wrapper import SearchPublicResponseWrapper

__all__ = ["CollectionResponseSearchPublicResponseWrapperNoPaging"]


class CollectionResponseSearchPublicResponseWrapperNoPaging(BaseModel):
    results: List[SearchPublicResponseWrapper]
