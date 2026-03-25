# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from .blog import Blog
from ...._models import BaseModel
from ...shared.version_user import VersionUser

__all__ = ["VersionBlog"]


class VersionBlog(BaseModel):
    id: str

    object: Blog

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The timestamp (ISO8601 format) when this blog version was updated."""

    user: VersionUser
