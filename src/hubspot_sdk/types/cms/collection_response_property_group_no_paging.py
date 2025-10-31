# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..crm.property_group import PropertyGroup

__all__ = ["CollectionResponsePropertyGroupNoPaging"]


class CollectionResponsePropertyGroupNoPaging(BaseModel):
    results: List[PropertyGroup]
