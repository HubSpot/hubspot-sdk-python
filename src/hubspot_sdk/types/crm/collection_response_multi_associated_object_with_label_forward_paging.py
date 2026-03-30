# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging
from .multi_associated_object_with_label import MultiAssociatedObjectWithLabel

__all__ = ["CollectionResponseMultiAssociatedObjectWithLabelForwardPaging"]


class CollectionResponseMultiAssociatedObjectWithLabelForwardPaging(BaseModel):
    results: List[MultiAssociatedObjectWithLabel]

    paging: Optional[ForwardPaging] = None
