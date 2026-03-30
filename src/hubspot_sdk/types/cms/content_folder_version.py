# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .content_folder import ContentFolder
from ..shared.version_user import VersionUser

__all__ = ["ContentFolderVersion"]


class ContentFolderVersion(BaseModel):
    id: str

    object: ContentFolder

    updated_at: datetime = FieldInfo(alias="updatedAt")

    user: VersionUser
