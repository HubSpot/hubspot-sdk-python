# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .property import Property
from ..._models import BaseModel

__all__ = ["CollectionResponsePropertyNoPaging"]


class CollectionResponsePropertyNoPaging(BaseModel):
    results: List[Property]
