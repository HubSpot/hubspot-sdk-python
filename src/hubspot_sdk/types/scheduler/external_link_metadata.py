# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExternalLinkMetadata"]


class ExternalLinkMetadata(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    default_link: bool = FieldInfo(alias="defaultLink")

    link: str

    organizer_user_id: str = FieldInfo(alias="organizerUserId")

    slug: str

    type: str

    user_ids_of_link_members: List[str] = FieldInfo(alias="userIdsOfLinkMembers")

    name: Optional[str] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
