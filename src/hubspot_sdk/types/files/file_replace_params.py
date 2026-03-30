# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["FileReplaceParams"]


class FileReplaceParams(TypedDict, total=False):
    charset_hunch: Annotated[str, PropertyInfo(alias="charsetHunch")]

    file: FileTypes

    options: str
