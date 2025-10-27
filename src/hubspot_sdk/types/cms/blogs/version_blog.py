# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from .blog import Blog
from ...._models import BaseModel
from ..version_user import VersionUser

__all__ = ["VersionBlog"]


class VersionBlog(BaseModel):
    id: str
    """The id of the version."""

    object: Blog

    updated_at: datetime = FieldInfo(alias="updatedAt")

    user: VersionUser
    """Model definition for a version user.

    Contains addition information about the user who created a version.
    """
