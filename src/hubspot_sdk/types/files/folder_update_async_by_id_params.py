# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FolderUpdateAsyncByIDParams"]


class FolderUpdateAsyncByIDParams(TypedDict, total=False):
    id: Required[str]
    """The unique identifier of the folder to be updated."""

    name: str
    """New name.

    If specified the folder's name and fullPath will change. All children of the
    folder will be updated accordingly.
    """

    parent_folder_id: Annotated[int, PropertyInfo(alias="parentFolderId")]
    """New parent folderId.

    If changed, the folder and all it's children will be moved into the specified
    folder. parentFolderId and parentFolderPath cannot be specified at the same
    time.
    """
