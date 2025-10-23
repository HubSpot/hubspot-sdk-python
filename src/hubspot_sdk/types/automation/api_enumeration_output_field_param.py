# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["APIEnumerationOutputFieldParam"]


class APIEnumerationOutputFieldParam(TypedDict, total=False):
    name: Required[str]

    options: Required[SequenceNotStr[str]]

    type: Required[Literal["ENUMERATION"]]
