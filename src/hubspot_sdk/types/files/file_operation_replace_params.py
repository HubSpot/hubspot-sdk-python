# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["FileOperationReplaceParams"]


class FileOperationReplaceParams(TypedDict, total=False):
    charset_hunch: Annotated[str, PropertyInfo(alias="charsetHunch")]
    """Character set of given file data."""

    file: FileTypes
    """File data that will replace existing file in the file manager."""

    options: str
    """JSON string representing FileReplaceOptions.

    Includes options to set the access and expiresAt properties, which will
    automatically update when the file is replaced.
    """
