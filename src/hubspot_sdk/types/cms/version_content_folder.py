# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .content_folder import ContentFolder
from ..shared.version_user import VersionUser

__all__ = ["VersionContentFolder"]


class VersionContentFolder(BaseModel):
    """Model definition for a content folder version.

    Contains metadata describing the version of the folder. It can be used to view edit history of a folder.
    """

    id: str
    """ID of this folder version."""

    object: ContentFolder
    """Model definition for a content folder."""

    updated_at: datetime = FieldInfo(alias="updatedAt")

    user: VersionUser
    """Model definition for a version user.

    Contains addition information about the user who created a version.
    """
