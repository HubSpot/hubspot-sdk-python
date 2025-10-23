# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EventDefinitionListParams"]


class EventDefinitionListParams(TypedDict, total=False):
    after: str
    """
    The paging cursor token of the last successfully read resource will be returned
    as the `paging.next.after` JSON property of a paged response containing more
    results.
    """

    include_properties: Annotated[bool, PropertyInfo(alias="includeProperties")]

    limit: int
    """The maximum number of results to display per page."""

    search_string: Annotated[str, PropertyInfo(alias="searchString")]
    """Characters in the event name that the user is searching for.

    This search is a naive “contains” search, no fuzzy matching is done.
    """

    sort_order: Annotated[str, PropertyInfo(alias="sortOrder")]
