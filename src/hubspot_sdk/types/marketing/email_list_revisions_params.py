# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["EmailListRevisionsParams"]


class EmailListRevisionsParams(TypedDict, total=False):
    after: str
    """The cursor token value to get the next set of results.

    You can get this from the `paging.next.after` JSON property of a paged response
    containing more results.
    """

    before: str
    """The cursor token value to get the previous set of results.

    You can get this from the `paging.prev.before` JSON property of a paged response
    containing more results.
    """

    limit: int
    """The maximum number of results to return. Default is 10."""
