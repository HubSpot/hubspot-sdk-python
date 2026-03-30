# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ActivityListSecurityActivitiesParams"]


class ActivityListSecurityActivitiesParams(TypedDict, total=False):
    after: str
    """The cursor token value to get the next set of results.

    You can get this from the `paging.next.after` JSON property of a paged response
    containing more results.
    """

    from_timestamp: Annotated[int, PropertyInfo(alias="fromTimestamp")]
    """Limit to activities created after this epoch timestamp."""

    limit: int
    """The maximum number of results to display per page. Max value of limit is 200."""

    to_timestamp: Annotated[int, PropertyInfo(alias="toTimestamp")]
    """Limit to activities created before this epoch timestamp."""

    user_id: Annotated[int, PropertyInfo(alias="userId")]
    """Identifier of user to retrieve activities for"""
