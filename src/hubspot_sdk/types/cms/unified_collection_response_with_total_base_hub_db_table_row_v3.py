# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .streaming_collection_response_with_total_hub_db_table_row_v3 import (
    StreamingCollectionResponseWithTotalHubDBTableRowV3,
)
from .random_access_collection_response_with_total_hub_db_table_row_v3 import (
    RandomAccessCollectionResponseWithTotalHubDBTableRowV3,
)

__all__ = ["UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3"]

UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3: TypeAlias = Union[
    RandomAccessCollectionResponseWithTotalHubDBTableRowV3, StreamingCollectionResponseWithTotalHubDBTableRowV3
]
