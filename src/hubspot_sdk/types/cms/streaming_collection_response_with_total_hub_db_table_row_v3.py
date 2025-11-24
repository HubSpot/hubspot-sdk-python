# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.paging import Paging

__all__ = ["StreamingCollectionResponseWithTotalHubDBTableRowV3"]


class StreamingCollectionResponseWithTotalHubDBTableRowV3(BaseModel):
    results: List[object]

    total: int
    """The total number of rows available in the collection."""

    type: Literal["STREAMING"]
    """Indicates the type of response, which is 'STREAMING' by default."""

    paging: Optional[Paging] = None
