# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .public_list import PublicList

__all__ = ["CollectionResponseWithTotalPublicListNoPaging"]


class CollectionResponseWithTotalPublicListNoPaging(BaseModel):
    results: List[PublicList]

    total: int
