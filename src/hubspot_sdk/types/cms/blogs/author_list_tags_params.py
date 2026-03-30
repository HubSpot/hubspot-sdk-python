# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["AuthorListTagsParams"]


class AuthorListTagsParams(TypedDict, total=False):
    after: str
    """
    The paging cursor token of the last successfully read resource will be returned
    as the `paging.next.after` JSON property of a paged response containing more
    results.
    """

    archived: bool
    """Whether to return only results that have been archived."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(alias="createdAfter", format="iso8601")]

    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]

    created_before: Annotated[Union[str, datetime], PropertyInfo(alias="createdBefore", format="iso8601")]

    limit: int
    """The maximum number of results to display per page."""

    property: str

    sort: SequenceNotStr[str]

    updated_after: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAfter", format="iso8601")]

    updated_at: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAt", format="iso8601")]

    updated_before: Annotated[Union[str, datetime], PropertyInfo(alias="updatedBefore", format="iso8601")]
