# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Folder"]


class Folder(BaseModel):
    id: str
    """ID of the folder."""

    archived: bool
    """Marks whether the folder is deleted or not."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp of folder creation."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp of the latest update to the folder."""

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)
    """Timestamp of folder deletion."""

    name: Optional[str] = None
    """Name of the folder."""

    parent_folder_id: Optional[str] = FieldInfo(alias="parentFolderId", default=None)
    """ID of the parent folder."""

    path: Optional[str] = None
    """Path of the folder in the file manager."""
