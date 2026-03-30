# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_email import PublicEmail
from ..shared.version_user import VersionUser

__all__ = ["VersionPublicEmail"]


class VersionPublicEmail(BaseModel):
    id: str
    """ID of this marketing email version."""

    object: PublicEmail

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The date and time of the last update to the email, in ISO8601 representation."""

    user: VersionUser
