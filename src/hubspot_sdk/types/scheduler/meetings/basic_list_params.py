# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["BasicListParams"]


class BasicListParams(TypedDict, total=False):
    after: str
    """
    The paging cursor token of the last successfully read resource will be returned
    as the `paging.next.after` JSON property of a paged response containing more
    results.
    """

    limit: int
    """The maximum number of results to display per page."""

    name: str

    organizer_user_id: Annotated[str, PropertyInfo(alias="organizerUserId")]

    type: Literal["GROUP_CALENDAR", "PERSONAL_LINK", "ROUND_ROBIN_CALENDAR"]
