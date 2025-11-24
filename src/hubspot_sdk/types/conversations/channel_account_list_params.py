# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ChannelAccountListParams"]


class ChannelAccountListParams(TypedDict, total=False):
    after: str

    archived: bool

    channel_id: Annotated[Iterable[int], PropertyInfo(alias="channelId")]

    default_page_length: Annotated[int, PropertyInfo(alias="defaultPageLength")]

    inbox_id: Annotated[Iterable[int], PropertyInfo(alias="inboxId")]

    limit: int

    sort: SequenceNotStr[str]
