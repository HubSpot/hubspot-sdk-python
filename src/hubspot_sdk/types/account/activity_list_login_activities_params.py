# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ActivityListLoginActivitiesParams"]


class ActivityListLoginActivitiesParams(TypedDict, total=False):
    after: str
    """The cursor token value to get the next set of results.

    You can get this from the `paging.next.after` JSON property of a paged response
    containing more results.
    """

    limit: int
    """The maximum number of results to display per page. Max value of limit is 200."""

    user_id: Annotated[int, PropertyInfo(alias="userId")]
    """The ID of a user, for retrieving user-specific logs."""
