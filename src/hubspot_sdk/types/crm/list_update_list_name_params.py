# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ListUpdateListNameParams"]


class ListUpdateListNameParams(TypedDict, total=False):
    include_filters: Annotated[bool, PropertyInfo(alias="includeFilters")]

    list_name: Annotated[str, PropertyInfo(alias="listName")]
