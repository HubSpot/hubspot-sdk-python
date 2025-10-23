# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from .filter_param import FilterParam

__all__ = ["PublicCRMSearchRequestParam"]


class PublicCRMSearchRequestParam(TypedDict, total=False):
    filters: Required[Iterable[FilterParam]]

    query: Required[str]

    sorts: Required[SequenceNotStr[str]]
