# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ContentFolder"]


class ContentFolder(BaseModel):
    id: str
    """The unique ID of the content folder."""

    category: int
    """The type of object this folder applies to. Should always be LANDING_PAGE."""

    created: datetime
    """The timestamp indicating when the content folder was created."""

    deleted_at: datetime = FieldInfo(alias="deletedAt")
    """The timestamp (ISO8601 format) when this content folder was deleted."""

    name: str
    """The name of the folder which will show up in the app dashboard"""

    parent_folder_id: int = FieldInfo(alias="parentFolderId")
    """The ID of the content folder this folder is nested under"""

    updated: datetime
    """The timestamp indicating when the content folder was last updated."""
