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
    """A marketing email"""

    updated_at: datetime = FieldInfo(alias="updatedAt")

    user: VersionUser
    """Model definition for a version user.

    Contains addition information about the user who created a version.
    """
