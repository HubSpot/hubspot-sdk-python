# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicMembershipSettingsParam"]


class PublicMembershipSettingsParam(TypedDict, total=False):
    include_unassigned: Annotated[bool, PropertyInfo(alias="includeUnassigned")]
    """Indicates whether unassigned memberships should be included."""

    membership_team_id: Annotated[int, PropertyInfo(alias="membershipTeamId")]
    """The ID of the team associated with the membership."""
