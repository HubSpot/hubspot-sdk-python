# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    after: str
    """
    The paging cursor token of the last successfully read resource will be returned
    as the `paging.next.after` JSON property of a paged response containing more
    results.
    """

    archived: bool
    """Whether to return only results that have been archived."""

    limit: int
    """The maximum number of results to display per page."""

    property: str
    """A specific property to include in the message response."""

    sort: SequenceNotStr[str]
    """Sort direction.

    Valid options are `createdAt` (ascending), and `-createdAt` (descending,
    default)
    """
