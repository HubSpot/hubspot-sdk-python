# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SimpleUser"]


class SimpleUser(BaseModel):
    id: str
    """The unique identifier for the user."""

    email: str
    """The email address of the user."""

    first_name: str = FieldInfo(alias="firstName")
    """The first name of the user."""

    last_name: str = FieldInfo(alias="lastName")
    """The last name of the user."""
