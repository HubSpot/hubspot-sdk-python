# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    id_property: Annotated[Literal["USER_ID", "EMAIL"], PropertyInfo(alias="idProperty")]
    """The name of a property with unique user values.

    Valid values are `USER_ID`(default) or `EMAIL`
    """

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """The first name of the user."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """The last name of the user."""

    primary_team_id: Annotated[str, PropertyInfo(alias="primaryTeamId")]
    """The user's primary team."""

    role_id: Annotated[str, PropertyInfo(alias="roleId")]
    """The user's role."""

    secondary_team_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="secondaryTeamIds")]
    """The user's additional teams."""
