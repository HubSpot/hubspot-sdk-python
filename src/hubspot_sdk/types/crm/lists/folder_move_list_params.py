# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["FolderMoveListParams"]


class FolderMoveListParams(TypedDict, total=False):
    list_id: Required[Annotated[str, PropertyInfo(alias="listId")]]
    """The Id of the list to move."""

    new_folder_id: Required[Annotated[str, PropertyInfo(alias="newFolderId")]]
    """The Id of folder to move the list to, the root folder is Id 0."""
