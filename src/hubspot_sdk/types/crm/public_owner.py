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
    """The unique identifier of the owner."""

    archived: bool
    """Indicates whether the owner is archived."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when the owner was created."""

    type: Literal["PERSON", "QUEUE"]
    """The type of the owner, which can be either PERSON or QUEUE."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The date and time when the owner was last updated."""

    email: Optional[str] = None
    """The email address of the owner."""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """The first name of the owner."""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """The last name of the owner."""

    teams: Optional[List[PublicTeam]] = None

    user_id: Optional[int] = FieldInfo(alias="userId", default=None)
    """The user ID of the owner."""

    user_id_including_inactive: Optional[int] = FieldInfo(alias="userIdIncludingInactive", default=None)
    """The user ID of the owner, including inactive users."""
