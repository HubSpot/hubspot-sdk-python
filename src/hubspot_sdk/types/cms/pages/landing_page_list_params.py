# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["LandingPageListParams"]


class LandingPageListParams(TypedDict, total=False):
    after: str
    """A cursor token for pagination.

    Use the value from the previous response's paging.next.after field.
    """

    archived: bool
    """Whether to return only results that have been archived."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(alias="createdAfter", format="iso8601")]
    """Filter landing pages created after a specific date and time."""

    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]
    """Filter landing pages by their creation timestamp."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(alias="createdBefore", format="iso8601")]
    """Filter landing pages created before a specific date and time."""

    limit: int
    """The maximum number of results to display per page."""

    property: str
    """Specify which properties of the landing pages to include in the response."""

    sort: SequenceNotStr[str]
    """Specify the order in which results are returned. Accepts an array of strings."""

    updated_after: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAfter", format="iso8601")]
    """Filter landing pages updated after a specific date and time."""

    updated_at: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAt", format="iso8601")]
    """Filter landing pages by their last updated timestamp."""

    updated_before: Annotated[Union[str, datetime], PropertyInfo(alias="updatedBefore", format="iso8601")]
    """Filter landing pages updated before a specific date and time."""
