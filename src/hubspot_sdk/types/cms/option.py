# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .simple_user import SimpleUser

__all__ = ["Option"]


class Option(BaseModel):
    """A HubSpot property option"""

    id: str
    """The unique ID of the option."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp when the option was created, in ISO 8601 format."""

    label: str
    """A user-friendly label that identifies the option."""

    name: str
    """An internal name assigned to the option, distinct from the label."""

    order: int
    """The order in which the option appears, represented as an integer."""

    type: str
    """Indicates the category or data type of the option (e.g., string, number)."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The timestamp when the option was last updated, in ISO 8601 format."""

    created_by: Optional[SimpleUser] = FieldInfo(alias="createdBy", default=None)

    created_by_user_id: Optional[int] = FieldInfo(alias="createdByUserId", default=None)
    """The ID of the user who created the option."""

    updated_by: Optional[SimpleUser] = FieldInfo(alias="updatedBy", default=None)

    updated_by_user_id: Optional[int] = FieldInfo(alias="updatedByUserId", default=None)
    """The ID of the user who last updated the option."""
