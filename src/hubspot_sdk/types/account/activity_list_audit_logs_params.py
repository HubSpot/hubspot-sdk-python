# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ActivityListAuditLogsParams"]


class ActivityListAuditLogsParams(TypedDict, total=False):
    acting_user_id: Annotated[Iterable[int], PropertyInfo(alias="actingUserId")]
    """The ID of a user, for retrieving user-specific logs."""

    after: str
    """
    The paging cursor token of the last successfully read resource will be returned
    as the `paging.next.after` JSON property of a paged response containing more
    results.
    """

    limit: int
    """The maximum number of results to display per page."""

    occurred_after: Annotated[Union[str, datetime], PropertyInfo(alias="occurredAfter", format="iso8601")]
    """A timestamp, as a starting point for retrieving activity logs."""

    occurred_before: Annotated[Union[str, datetime], PropertyInfo(alias="occurredBefore", format="iso8601")]
    """A timestamp, as an end point for retrieving activity logs."""

    sort: SequenceNotStr[str]
    """Set to `occurredAt` to order results by the time of the event.

    By default, events are ordered from oldest to newest.
    """
