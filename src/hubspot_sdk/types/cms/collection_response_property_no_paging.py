# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .property_1 import Property1

__all__ = ["CollectionResponsePropertyNoPaging"]


class CollectionResponsePropertyNoPaging(BaseModel):
    results: List[Property1]
