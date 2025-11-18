# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["MeetingsLinkListParams"]


class MeetingsLinkListParams(TypedDict, total=False):
    after: str
    """
    The paging cursor token of the last successfully read resource will be returned
    as the `paging.next.after` JSON property of a paged response containing more
    results.
    """

    limit: int
    """The maximum number of results to display per page."""

    name: str
    """Retrieve scheduling pages with a specified name."""

    organizer_user_id: Annotated[str, PropertyInfo(alias="organizerUserId")]
    """Filter the response to scheduling pages created by the specified user."""

    type: str
    """Filter the response to the specific type of meeting."""
