# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FileAssetCreateParams"]


class FileAssetCreateParams(TypedDict, total=False):
    name: Required[str]
    """Desired name for the folder."""

    parent_folder_id: Annotated[str, PropertyInfo(alias="parentFolderId")]
    """FolderId of the parent of the created folder.

    If not specified, the folder will be created at the root level. parentFolderId
    and parentFolderPath cannot be set at the same time.
    """

    parent_path: Annotated[str, PropertyInfo(alias="parentPath")]
    """Path of the parent of the created folder.

    If not specified the folder will be created at the root level. parentFolderPath
    and parentFolderId cannot be set at the same time.
    """
