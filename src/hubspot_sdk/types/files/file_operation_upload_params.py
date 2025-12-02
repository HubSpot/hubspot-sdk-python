# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["FileOperationUploadParams"]


class FileOperationUploadParams(TypedDict, total=False):
    charset_hunch: Annotated[str, PropertyInfo(alias="charsetHunch")]
    """Character set of the uploaded file."""

    file: FileTypes
    """File to be uploaded."""

    file_name: Annotated[str, PropertyInfo(alias="fileName")]
    """Desired name for the uploaded file."""

    folder_id: Annotated[str, PropertyInfo(alias="folderId")]
    """Either 'folderId' or 'folderPath' is required.

    folderId is the ID of the folder the file will be uploaded to.
    """

    folder_path: Annotated[str, PropertyInfo(alias="folderPath")]
    """Either 'folderPath' or 'folderId' is required.

    This field represents the destination folder path for the uploaded file. If a
    path doesn't exist, the system will try to create one.
    """

    options: str
    """JSON string representing FileUploadOptions."""
