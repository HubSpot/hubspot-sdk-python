# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..marketing.paging import Paging
from .multi_associated_object_with_label import MultiAssociatedObjectWithLabel

__all__ = ["CollectionResponseMultiAssociatedObjectWithLabel"]


class CollectionResponseMultiAssociatedObjectWithLabel(BaseModel):
    results: List[MultiAssociatedObjectWithLabel]

    paging: Optional[Paging] = None
    """Contains information pagination of results."""
