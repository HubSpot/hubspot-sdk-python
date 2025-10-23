# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ...._types import SequenceNotStr

__all__ = ["RowListDraftParams"]


class RowListDraftParams(TypedDict, total=False):
    after: str
    """The cursor token value to get the next set of results.

    You can get this from the `paging.next.after` JSON property of a paged response
    containing more results.
    """

    archived: bool

    limit: int
    """The maximum number of results to return. Default is `1000`."""

    offset: int

    properties: SequenceNotStr[str]
    """
    Specify the column names to get results containing only the required columns
    instead of all column details. If you want to include multiple columns in the
    result, use this query param as many times.
    """

    sort: SequenceNotStr[str]
    """Specifies the column names to sort the results by."""
