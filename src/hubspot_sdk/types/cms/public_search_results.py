# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .content_search_result import ContentSearchResult

__all__ = ["PublicSearchResults"]


class PublicSearchResults(BaseModel):
    limit: int

    offset: int

    page: int

    results: List[ContentSearchResult]

    total: int

    search_term: Optional[str] = FieldInfo(alias="searchTerm", default=None)
