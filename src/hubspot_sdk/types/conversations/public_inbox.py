# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicInbox"]


class PublicInbox(BaseModel):
    id: str

    archived: bool

    created_at: datetime = FieldInfo(alias="createdAt")

    name: str

    type: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)
