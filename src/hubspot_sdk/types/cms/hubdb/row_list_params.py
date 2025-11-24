# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ...._types import SequenceNotStr

__all__ = ["RowListParams"]


class RowListParams(TypedDict, total=False):
    after: str
    """The cursor token value to get the next set of results.

    You can get this from the `paging.next.after` JSON property of a paged response
    containing more results.
    """

    archived: bool
    """Specifies whether to include archived rows in the response."""

    limit: int
    """The maximum number of results to return. Default is `1000`."""

    offset: int
    """The number of rows to skip before starting to return results."""

    properties: SequenceNotStr[str]
    """
    Specify the column names to get results containing only the required columns
    instead of all column details.
    """

    sort: SequenceNotStr[str]
    """Specifies the column names to sort the results by.

    See the above description for more details.
    """
