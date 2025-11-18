# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ChannelAccountListParams"]


class ChannelAccountListParams(TypedDict, total=False):
    after: str
    """
    The paging cursor token of the last successfully read resource will be returned
    as the `paging.next.after` JSON property of a paged response containing more
    results.
    """

    archived: bool
    """Whether to include archived channel accounts in the response."""

    channel_id: Annotated[Iterable[int], PropertyInfo(alias="channelId")]
    """Limits results to channel accounts within a particular channel."""

    default_page_length: Annotated[int, PropertyInfo(alias="defaultPageLength")]
    """The default number of results to display per page."""

    inbox_id: Annotated[Iterable[int], PropertyInfo(alias="inboxId")]
    """Limits results to channel accounts within a particular inbox."""

    limit: int
    """The maximum number of results to display per page."""

    sort: SequenceNotStr[str]
    """The sort order for the channel accounts."""
