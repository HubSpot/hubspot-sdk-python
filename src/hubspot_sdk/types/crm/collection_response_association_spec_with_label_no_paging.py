# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .association_spec_with_label import AssociationSpecWithLabel

__all__ = ["CollectionResponseAssociationSpecWithLabelNoPaging"]


class CollectionResponseAssociationSpecWithLabelNoPaging(BaseModel):
    results: List[AssociationSpecWithLabel]
