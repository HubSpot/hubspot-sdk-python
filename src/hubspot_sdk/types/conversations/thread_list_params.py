# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ThreadListParams"]


class ThreadListParams(TypedDict, total=False):
    after: str
    """
    The paging cursor token of the last successfully read resource will be returned
    as the `paging.next.after` JSON property of a paged response containing more
    results.
    """

    archived: bool
    """Whether to return only results that have been archived."""

    associated_contact_id: Annotated[int, PropertyInfo(alias="associatedContactId")]
    """Retrieve a filtered list of conversations for a specific contact by its ID.

    This parameter cannot be used in conjunction with the `inboxId` property.
    """

    association: List[Literal["TICKET"]]
    """You can specify an association type here of `TICKET`.

    If this is set the response will included a thread associations object and
    associated ticket id if present. If there are no associations to a ticket with
    this conversation, then the thread associations object will not be present on
    the response.
    """

    inbox_id: Annotated[Iterable[int], PropertyInfo(alias="inboxId")]
    """
    The ID of the conversations inbox you can optionally include to retrieve the
    associated messages for. This parameter cannot be used in conjunction with the
    `associatedContactId` property.
    """

    latest_message_timestamp_after: Annotated[
        Union[str, datetime], PropertyInfo(alias="latestMessageTimestampAfter", format="iso8601")
    ]
    """The minimum(earliest) `latestMessageTimestamp`.

    This is required only when sorting by `latestMessageTimestamp`.
    """

    limit: int
    """The maximum number of results to display per page."""

    property: str
    """A specific property to include in the thread response."""

    sort: SequenceNotStr[str]
    """Set the sort order of the response.

    Valid options are `id` (default) and `latestMessageTimestamp` (which requires
    the `latestMessageTimestampAfter` field to also be set). If you’re filtering
    threads by `associatedContactId` , you can sort in descending order by
    prepending - to the sort option (e.g., `-id` or `-latestMessageTimestampAfter`
    ). Otherwise, results are always returned in ascending order.
    """

    thread_status: Annotated[str, PropertyInfo(alias="threadStatus")]
    """
    The status of the associated conversations to filter by (either `OPEN` or
    `CLOSED`). This property must be provided if you’re including the
    `associatedContactId` query parameter.
    """
