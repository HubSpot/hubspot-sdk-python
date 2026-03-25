# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .association_label_limit_response import AssociationLabelLimitResponse

__all__ = ["CollectionResponseAssociationLabelLimitResponseNoPaging"]


class CollectionResponseAssociationLabelLimitResponseNoPaging(BaseModel):
    results: List[AssociationLabelLimitResponse]
