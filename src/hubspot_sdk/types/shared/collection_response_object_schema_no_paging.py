# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..crm.objects.object_schema import ObjectSchema

__all__ = ["CollectionResponseObjectSchemaNoPaging"]


class CollectionResponseObjectSchemaNoPaging(BaseModel):
    results: List[ObjectSchema]
