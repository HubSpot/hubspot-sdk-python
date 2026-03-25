# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RecordListMembership"]


class RecordListMembership(BaseModel):
    first_added_timestamp: datetime = FieldInfo(alias="firstAddedTimestamp")
    """The timestamp when the record was first added to the list."""

    last_added_timestamp: datetime = FieldInfo(alias="lastAddedTimestamp")
    """The timestamp when the record was last added to the list."""

    list_id: str = FieldInfo(alias="listId")
    """The unique identifier of the list."""

    list_version: int = FieldInfo(alias="listVersion")
    """The version number of the list."""

    is_public_list: Optional[bool] = FieldInfo(alias="isPublicList", default=None)
    """Indicates whether the list is public."""
