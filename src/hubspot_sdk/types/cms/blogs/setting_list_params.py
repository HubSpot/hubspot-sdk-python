# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["SettingListParams"]


class SettingListParams(TypedDict, total=False):
    after: str
    """The cursor token value to get the next set of results.

    You can get this from the `paging.next.after` JSON property of a paged response
    containing more results.
    """

    archived: bool
    """Specifies whether to return archived Blogs. Defaults to `false`."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(alias="createdAfter", format="iso8601")]
    """Only return Blogs created after the specified time."""

    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]
    """Only return Blogs created at exactly the specified time."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(alias="createdBefore", format="iso8601")]
    """Only return Blogs created before the specified time."""

    limit: int
    """The maximum number of results to return. Default is 100."""

    sort: SequenceNotStr[str]
    """Specifies which fields to use for sorting results.

    Valid fields are `name` and `id`
    """

    updated_after: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAfter", format="iso8601")]
    """Only return Blogs last updated after the specified time."""

    updated_at: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAt", format="iso8601")]
    """Only return Blogs last updated at exactly the specified time."""

    updated_before: Annotated[Union[str, datetime], PropertyInfo(alias="updatedBefore", format="iso8601")]
    """Only return Blogs last updated before the specified time."""
