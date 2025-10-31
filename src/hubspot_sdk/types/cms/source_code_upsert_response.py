# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SourceCodeUpsertResponse"]


class SourceCodeUpsertResponse(BaseModel):
    id: str
    """The path of the file in the CMS Developer File System."""

    created_at: int = FieldInfo(alias="createdAt")
    """Timestamp of when the object was first created."""

    folder: bool
    """Determines whether or not this path points to a folder."""

    name: str
    """The name of the file."""

    updated_at: int = FieldInfo(alias="updatedAt")
    """Timestamp of when the object was last updated."""

    archived_at: Optional[int] = FieldInfo(alias="archivedAt", default=None)
    """Timestamp of when the object was archived (deleted)."""

    children: Optional[List[str]] = None
    """
    If the object is a folder, contains the filenames of the files within the
    folder.
    """

    hash: Optional[str] = None
