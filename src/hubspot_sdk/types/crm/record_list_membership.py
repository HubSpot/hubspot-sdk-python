# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RecordListMembership"]


class RecordListMembership(BaseModel):
    """Lists record is member of"""

    list_id: str = FieldInfo(alias="listId")

    list_version: int = FieldInfo(alias="listVersion")

    first_added_timestamp: Optional[datetime] = FieldInfo(alias="firstAddedTimestamp", default=None)

    is_public_list: Optional[bool] = FieldInfo(alias="isPublicList", default=None)

    last_added_timestamp: Optional[datetime] = FieldInfo(alias="lastAddedTimestamp", default=None)
