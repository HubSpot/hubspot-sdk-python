# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicUser"]


class PublicUser(BaseModel):
    """A user"""

    id: str
    """The user's unique ID."""

    email: str
    """The user's email."""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """The user's first name."""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """The user's last name."""

    primary_team_id: Optional[str] = FieldInfo(alias="primaryTeamId", default=None)
    """The user's primary team"""

    role_id: Optional[str] = FieldInfo(alias="roleId", default=None)
    """The user's role."""

    role_ids: Optional[List[str]] = FieldInfo(alias="roleIds", default=None)
    """A list of role IDs assigned to the user."""

    secondary_team_ids: Optional[List[str]] = FieldInfo(alias="secondaryTeamIds", default=None)
    """The user's additional teams."""

    send_welcome_email: Optional[bool] = FieldInfo(alias="sendWelcomeEmail", default=None)
    """Whether a welcome email was sent to the user.

    This value will only be populated in response to a provisioning request.
    Subsequent queries will be false.
    """

    super_admin: Optional[bool] = FieldInfo(alias="superAdmin", default=None)
    """Whether the user has super admin privileges."""
