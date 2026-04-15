# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..shared.property import Property

__all__ = ["CollectionResponsePropertyNoPaging"]


class CollectionResponsePropertyNoPaging(BaseModel):
    results: List[Property]
