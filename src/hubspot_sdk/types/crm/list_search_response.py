# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_object_list_search_result import PublicObjectListSearchResult

__all__ = ["ListSearchResponse"]


class ListSearchResponse(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")
    """Whether or not there are more results to page through."""

    lists: List[PublicObjectListSearchResult]
    """The lists that matched the search criteria."""

    offset: int
    """Value to be passed in a future request to paginate through list search results."""

    total: int
    """The total number of lists that match the search criteria."""
