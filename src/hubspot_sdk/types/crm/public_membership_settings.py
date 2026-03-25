# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicMembershipSettings"]


class PublicMembershipSettings(BaseModel):
    include_unassigned: Optional[bool] = FieldInfo(alias="includeUnassigned", default=None)
    """Indicates whether unassigned memberships should be included."""

    membership_team_id: Optional[int] = FieldInfo(alias="membershipTeamId", default=None)
    """The ID of the team associated with the membership."""
