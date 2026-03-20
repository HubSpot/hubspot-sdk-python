# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging
from .simple_public_object_with_associations import SimplePublicObjectWithAssociations

__all__ = ["CollectionResponseSimplePublicObjectWithAssociationsForwardPaging"]


class CollectionResponseSimplePublicObjectWithAssociationsForwardPaging(BaseModel):
    results: List[SimplePublicObjectWithAssociations]

    paging: Optional[ForwardPaging] = None
