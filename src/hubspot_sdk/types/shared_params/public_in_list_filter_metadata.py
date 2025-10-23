# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicInListFilterMetadata"]


class PublicInListFilterMetadata(TypedDict, total=False):
    id: Required[str]

    in_list_type: Required[Annotated[str, PropertyInfo(alias="inListType")]]
