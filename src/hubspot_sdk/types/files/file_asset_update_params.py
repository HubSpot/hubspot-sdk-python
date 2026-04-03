# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FileAssetUpdateParams"]


class FileAssetUpdateParams(TypedDict, total=False):
    clear_expires: Required[Annotated[bool, PropertyInfo(alias="clearExpires")]]

    access: Literal[
        "HIDDEN_INDEXABLE",
        "HIDDEN_NOT_INDEXABLE",
        "HIDDEN_PRIVATE",
        "HIDDEN_SENSITIVE",
        "PRIVATE",
        "PUBLIC_INDEXABLE",
        "PUBLIC_NOT_INDEXABLE",
        "SENSITIVE",
    ]
    """NONE: Do not run any duplicate validation.

    REJECT: Reject the upload if a duplicate is found. RETURN_EXISTING: If a
    duplicate file is found, do not upload a new file and return the found duplicate
    instead.
    """

    expires_at: Annotated[Union[str, datetime], PropertyInfo(alias="expiresAt", format="iso8601")]

    is_usable_in_content: Annotated[bool, PropertyInfo(alias="isUsableInContent")]
    """Mark whether the file should be used in new content or not."""

    name: str
    """New name for the file."""

    parent_folder_id: Annotated[str, PropertyInfo(alias="parentFolderId")]
    """FolderId where the file should be moved to.

    folderId and folderPath parameters cannot be set at the same time.
    """

    parent_folder_path: Annotated[str, PropertyInfo(alias="parentFolderPath")]
    """Folder path where the file should be moved to.

    folderId and folderPath parameters cannot be set at the same time.
    """
