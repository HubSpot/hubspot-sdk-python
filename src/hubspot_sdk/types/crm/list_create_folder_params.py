# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ListCreateFolderParams"]


class ListCreateFolderParams(TypedDict, total=False):
    name: Required[str]
    """The name of the folder to be created."""

    parent_folder_id: Annotated[str, PropertyInfo(alias="parentFolderId")]
    """
    The folder this should be created in, if not specified will be created in the
    root folder 0.
    """
