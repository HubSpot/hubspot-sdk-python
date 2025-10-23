# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..settings.public_team import PublicTeam

__all__ = ["PublicOwner"]


class PublicOwner(BaseModel):
    id: str

    archived: bool

    created_at: datetime = FieldInfo(alias="createdAt")

    type: Literal["PERSON", "QUEUE"]

    updated_at: datetime = FieldInfo(alias="updatedAt")

    email: Optional[str] = None

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    teams: Optional[List[PublicTeam]] = None

    user_id: Optional[int] = FieldInfo(alias="userId", default=None)

    user_id_including_inactive: Optional[int] = FieldInfo(alias="userIdIncludingInactive", default=None)
