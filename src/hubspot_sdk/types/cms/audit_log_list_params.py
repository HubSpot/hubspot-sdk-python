# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["AuditLogListParams"]


class AuditLogListParams(TypedDict, total=False):
    after: str
    """
    The paging cursor token of the last successfully read resource will be returned
    as the `paging.next.after` JSON property of a paged response containing more
    results.
    """

    before: str

    event_type: Annotated[SequenceNotStr[str], PropertyInfo(alias="eventType")]

    limit: int
    """The maximum number of results to display per page."""

    object_id: Annotated[SequenceNotStr[str], PropertyInfo(alias="objectId")]

    object_type: Annotated[SequenceNotStr[str], PropertyInfo(alias="objectType")]

    sort: SequenceNotStr[str]

    user_id: Annotated[SequenceNotStr[str], PropertyInfo(alias="userId")]
