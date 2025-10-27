# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..marketing.paging import Paging
from .simple_public_object_with_associations import SimplePublicObjectWithAssociations

__all__ = ["CollectionResponseSimplePublicObjectWithAssociations"]


class CollectionResponseSimplePublicObjectWithAssociations(BaseModel):
    results: List[SimplePublicObjectWithAssociations]

    paging: Optional[Paging] = None
    """Contains information pagination of results."""
