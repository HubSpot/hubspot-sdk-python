# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .bounded_paging import BoundedPaging

__all__ = ["RandomAccessCollectionResponseWithTotalHubDBTableRowV3"]


class RandomAccessCollectionResponseWithTotalHubDBTableRowV3(BaseModel):
    results: List[object]

    total: int
    """The total number of rows available in the collection."""

    type: Literal["RANDOM_ACCESS"]
    """Indicates the type of response, which is 'RANDOM_ACCESS' by default."""

    paging: Optional[BoundedPaging] = None
