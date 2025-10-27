# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicInbox"]


class PublicInbox(BaseModel):
    archived: bool

    type: str
    """Specifies whether this refers to a Conversations Inbox or to the Help Desk.

    Valid values are INBOX or HELP_DESK
    """

    id: Optional[str] = None
    """The ID of the inbox."""

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """When the inbox was created."""

    name: Optional[str] = None
    """The name of the inbox."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
