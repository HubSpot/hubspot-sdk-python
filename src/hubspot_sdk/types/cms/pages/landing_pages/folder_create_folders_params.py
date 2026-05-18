# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ...content_folder_param import ContentFolderParam

__all__ = ["FolderCreateFoldersParams"]


class FolderCreateFoldersParams(TypedDict, total=False):
    inputs: Required[Iterable[ContentFolderParam]]
    """Content folders to input."""
