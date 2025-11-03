# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..marketing.emails_paging import EmailsPaging
from .simple_public_object_with_associations import SimplePublicObjectWithAssociations

__all__ = ["CollectionResponseSimplePublicObjectWithAssociations"]


class CollectionResponseSimplePublicObjectWithAssociations(BaseModel):
    results: List[SimplePublicObjectWithAssociations]

    paging: Optional[EmailsPaging] = None
    """Contains information pagination of results."""
