# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ListGetByObjectTypeAndNameParams"]


class ListGetByObjectTypeAndNameParams(TypedDict, total=False):
    object_type_id: Required[Annotated[str, PropertyInfo(alias="objectTypeId")]]

    include_filters: Annotated[bool, PropertyInfo(alias="includeFilters")]
