# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicTeam"]


class PublicTeam(BaseModel):
    id: str
    """The team's unique ID"""

    name: str
    """The team's name"""

    secondary_user_ids: List[str] = FieldInfo(alias="secondaryUserIds")
    """Secondary or additional members of this team"""

    user_ids: List[str] = FieldInfo(alias="userIds")
    """Primary members of this team"""
