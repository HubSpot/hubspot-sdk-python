# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicInbox"]


class PublicInbox(BaseModel):
    id: str
    """The ID of the inbox."""

    archived: bool

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the inbox was created."""

    name: str
    """The name of the inbox."""

    type: str
    """Specifies whether this refers to a Conversations Inbox or to the Help Desk.

    Valid values are INBOX or HELP_DESK
    """

    updated_at: datetime = FieldInfo(alias="updatedAt")

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)
