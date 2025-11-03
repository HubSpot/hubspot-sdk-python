# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .filter_param import FilterParam
from .filter_group_param import FilterGroupParam

__all__ = ["PublicCrmSearchRequestParam"]


class PublicCrmSearchRequestParam(TypedDict, total=False):
    filter_groups: Required[Annotated[Iterable[FilterGroupParam], PropertyInfo(alias="filterGroups")]]

    filters: Required[Iterable[FilterParam]]

    sorts: Required[SequenceNotStr[str]]

    query: str
