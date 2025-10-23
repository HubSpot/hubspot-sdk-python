# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicListPermissionsParam"]


class PublicListPermissionsParam(TypedDict, total=False):
    teams_with_edit_access: Required[Annotated[Iterable[int], PropertyInfo(alias="teamsWithEditAccess")]]

    users_with_edit_access: Required[Annotated[Iterable[int], PropertyInfo(alias="usersWithEditAccess")]]
