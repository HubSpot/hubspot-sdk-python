# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["ImportCreateParams"]


class ImportCreateParams(TypedDict, total=False):
    files: FileTypes

    import_request: Annotated[str, PropertyInfo(alias="importRequest")]
