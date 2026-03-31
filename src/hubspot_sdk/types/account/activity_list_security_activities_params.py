# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ActivityListSecurityActivitiesParams"]


class ActivityListSecurityActivitiesParams(TypedDict, total=False):
    after: str
    """
    The paging cursor token of the last successfully read resource will be returned
    as the `paging.next.after` JSON property of a paged response containing more
    results.
    """

    from_timestamp: Annotated[int, PropertyInfo(alias="fromTimestamp")]

    limit: int
    """The maximum number of results to display per page."""

    to_timestamp: Annotated[int, PropertyInfo(alias="toTimestamp")]

    user_id: Annotated[int, PropertyInfo(alias="userId")]
