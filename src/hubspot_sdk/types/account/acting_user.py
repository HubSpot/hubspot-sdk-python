# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ActingUser"]


class ActingUser(BaseModel):
    user_id: int = FieldInfo(alias="userId")
    """The ID of the user who performed the action."""

    user_email: Optional[str] = FieldInfo(alias="userEmail", default=None)
    """The email address of the user who performed the action."""
