# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .object_type_near_or_at_association_limit import ObjectTypeNearOrAtAssociationLimit

__all__ = ["CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging"]


class CollectionResponseObjectTypeNearOrAtAssociationLimitNoPaging(BaseModel):
    results: List[ObjectTypeNearOrAtAssociationLimit]
