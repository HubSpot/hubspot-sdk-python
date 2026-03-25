# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FolderUpdateAsyncByIDParams"]


class FolderUpdateAsyncByIDParams(TypedDict, total=False):
    id: Required[str]
    """The unique identifier of the folder to be updated."""

    name: str
    """
    The new name for the folder, which will also update the fullPath and all
    children of the folder.
    """

    parent_folder_id: Annotated[int, PropertyInfo(alias="parentFolderId")]
    """
    The ID of the new parent folder, which will move the folder and its children
    into the specified folder.
    """
