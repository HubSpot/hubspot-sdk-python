# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RecordListMembership"]


class RecordListMembership(BaseModel):
    first_added_timestamp: datetime = FieldInfo(alias="firstAddedTimestamp")

    last_added_timestamp: datetime = FieldInfo(alias="lastAddedTimestamp")

    list_id: str = FieldInfo(alias="listId")

    list_version: int = FieldInfo(alias="listVersion")

    is_public_list: Optional[bool] = FieldInfo(alias="isPublicList", default=None)
