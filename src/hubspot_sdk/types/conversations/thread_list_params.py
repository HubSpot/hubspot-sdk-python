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

    archived: bool

    associated_contact_id: Annotated[int, PropertyInfo(alias="associatedContactId")]

    association: List[Literal["TICKET"]]

    inbox_id: Annotated[Iterable[int], PropertyInfo(alias="inboxId")]

    latest_message_timestamp_after: Annotated[
        Union[str, datetime], PropertyInfo(alias="latestMessageTimestampAfter", format="iso8601")
    ]

    limit: int

    property: str

    sort: SequenceNotStr[str]

    thread_status: Annotated[str, PropertyInfo(alias="threadStatus")]
