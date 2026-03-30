# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["FileUploadParams"]


class FileUploadParams(TypedDict, total=False):
    charset_hunch: Annotated[str, PropertyInfo(alias="charsetHunch")]

    file: FileTypes

    file_name: Annotated[str, PropertyInfo(alias="fileName")]

    folder_id: Annotated[str, PropertyInfo(alias="folderId")]

    folder_path: Annotated[str, PropertyInfo(alias="folderPath")]

    options: str
