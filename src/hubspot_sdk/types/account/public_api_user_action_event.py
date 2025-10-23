# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .acting_user import ActingUser

__all__ = ["PublicAPIUserActionEvent"]


class PublicAPIUserActionEvent(BaseModel):
    id: str
    """The unique ID of the activity."""

    acting_user: ActingUser = FieldInfo(alias="actingUser")

    action: str
    """The type of action taken."""

    category: str
    """The category of the activity."""

    occurred_at: datetime = FieldInfo(alias="occurredAt")
    """The time that the action occurred at."""

    sub_category: Optional[str] = FieldInfo(alias="subCategory", default=None)
    """The subcategory of the activity."""

    target_object_id: Optional[str] = FieldInfo(alias="targetObjectId", default=None)
    """The ID of the impacted object."""
