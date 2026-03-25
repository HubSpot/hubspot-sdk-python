# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .content_search_result import ContentSearchResult

__all__ = ["PublicSearchResults"]


class PublicSearchResults(BaseModel):
    limit: int
    """The number of results returned in a single response."""

    offset: int
    """The starting point for the next set of results in pagination."""

    page: int
    """The current page number in the paginated results."""

    results: List[ContentSearchResult]

    total: int
    """The total number of results found for the search term."""

    search_term: Optional[str] = FieldInfo(alias="searchTerm", default=None)
    """The term used in the search query."""
