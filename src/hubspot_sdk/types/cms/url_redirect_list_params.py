# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["URLRedirectListParams"]


class URLRedirectListParams(TypedDict, total=False):
    after: str
    """A cursor token for pagination.

    Use the value from the previous response's paging.next.after field.
    """

    archived: bool
    """Whether to return only results that have been archived."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(alias="createdAfter", format="iso8601")]
    """Filter redirects created after a specific timestamp. Format must be date-time."""

    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]
    """Filter redirects by their exact creation timestamp. Format must be date-time."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(alias="createdBefore", format="iso8601")]
    """Filter redirects created before a specific timestamp. Format must be date-time."""

    limit: int
    """The maximum number of results to display per page."""

    sort: SequenceNotStr[str]
    """Specify the order in which to sort the results. Accepts an array of strings."""

    updated_after: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAfter", format="iso8601")]
    """Filter redirects updated after a specific timestamp. Format must be date-time."""

    updated_at: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAt", format="iso8601")]
    """Filter redirects by their exact update timestamp. Format must be date-time."""

    updated_before: Annotated[Union[str, datetime], PropertyInfo(alias="updatedBefore", format="iso8601")]
    """Filter redirects updated before a specific timestamp. Format must be date-time."""
