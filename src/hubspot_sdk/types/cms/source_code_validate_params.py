# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["SourceCodeValidateParams"]


class SourceCodeValidateParams(TypedDict, total=False):
    environment: Required[str]

    file: FileTypes
