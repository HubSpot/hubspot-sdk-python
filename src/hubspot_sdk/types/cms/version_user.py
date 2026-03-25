# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["VersionUser"]


class VersionUser(BaseModel):
    id: str
    """The unique ID of the User."""

    email: str
    """The email address of the user."""

    full_name: str = FieldInfo(alias="fullName")
    """The first and last name of the User."""
