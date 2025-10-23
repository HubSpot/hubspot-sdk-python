# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .public_in_list_filter_metadata import PublicInListFilterMetadata

__all__ = ["PublicInListFilter"]


class PublicInListFilter(TypedDict, total=False):
    filter_type: Required[Annotated[Literal["IN_LIST"], PropertyInfo(alias="filterType")]]

    list_id: Required[Annotated[str, PropertyInfo(alias="listId")]]

    operator: Required[str]

    metadata: PublicInListFilterMetadata
