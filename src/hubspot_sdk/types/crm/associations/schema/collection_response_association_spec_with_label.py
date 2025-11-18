# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel
from ....shared.paging import Paging
from ...association_spec_with_label import AssociationSpecWithLabel

__all__ = ["CollectionResponseAssociationSpecWithLabel"]


class CollectionResponseAssociationSpecWithLabel(BaseModel):
    results: List[AssociationSpecWithLabel]

    paging: Optional[Paging] = None
