# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["AuditLogListParams"]


class AuditLogListParams(TypedDict, total=False):
    after: str
    """Timestamp after which audit logs will be returned"""

    before: str
    """Timestamp before which audit logs will be returned"""

    event_type: Annotated[SequenceNotStr[str], PropertyInfo(alias="eventType")]
    """
    Comma separated list of event types to filter by (CREATED, UPDATED, PUBLISHED,
    DELETED, UNPUBLISHED).
    """

    limit: int
    """The number of logs to return."""

    object_id: Annotated[SequenceNotStr[str], PropertyInfo(alias="objectId")]
    """Comma separated list of object ids to filter by."""

    object_type: Annotated[SequenceNotStr[str], PropertyInfo(alias="objectType")]
    """
    Comma separated list of object types to filter by (BLOG, LANDING_PAGE, DOMAIN,
    HUBDB_TABLE etc.)
    """

    sort: SequenceNotStr[str]
    """The sort direction for the audit logs. (Can only sort by timestamp)."""

    user_id: Annotated[SequenceNotStr[str], PropertyInfo(alias="userId")]
    """Comma separated list of user ids to filter by."""
