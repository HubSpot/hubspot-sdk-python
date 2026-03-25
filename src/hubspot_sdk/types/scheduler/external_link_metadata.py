# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExternalLinkMetadata"]


class ExternalLinkMetadata(BaseModel):
    id: str
    """The unique identifier for the meeting link."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The Unix time in milliseconds when the meeting link was created."""

    default_link: bool = FieldInfo(alias="defaultLink")
    """Whether the meeting link is the user's default link."""

    link: str
    """The URL of the meeting link."""

    organizer_user_id: str = FieldInfo(alias="organizerUserId")
    """The user ID of the meeting link's organizer."""

    slug: str
    """The slug of the meeting link, located directly after the domain in the URL."""

    type: Literal["GROUP_CALENDAR", "PERSONAL_LINK", "ROUND_ROBIN_CALENDAR"]
    """The type of the external meeting link.

    Accepted values are: PERSONAL_LINK, GROUP_CALENDAR, ROUND_ROBIN_CALENDAR.
    """

    user_ids_of_link_members: List[str] = FieldInfo(alias="userIdsOfLinkMembers")

    name: Optional[str] = None
    """The name of the meeting link."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """The Unix time in milliseconds when the meeting link was last updated."""
