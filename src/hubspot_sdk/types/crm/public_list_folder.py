# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicListFolder"]


class PublicListFolder(BaseModel):
    id: str
    """The Id of the folder."""

    child_lists: List[int] = FieldInfo(alias="childLists")
    """An array of list Id's contained in this folder."""

    child_nodes: List["PublicListFolder"] = FieldInfo(alias="childNodes")

    parent_folder_id: str = FieldInfo(alias="parentFolderId")
    """The Id of the folder this folder is in, the root folder is represented as 0."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The time the folder was created at."""

    name: Optional[str] = None
    """The name of the folder."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """The time the folder was last updated at."""

    updated_contents_at: Optional[datetime] = FieldInfo(alias="updatedContentsAt", default=None)
    """The time that the contents of the folder was last updated at."""

    user_id: Optional[int] = FieldInfo(alias="userId", default=None)
    """The user Id of the owner of the folder."""
