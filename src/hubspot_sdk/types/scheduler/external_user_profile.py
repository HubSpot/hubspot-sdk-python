# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExternalUserProfile"]


class ExternalUserProfile(BaseModel):
    email: str
    """The email address of the user."""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """The first name of the user."""

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)
    """The full name of the user."""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """The last name of the user."""
