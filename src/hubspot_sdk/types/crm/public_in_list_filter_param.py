# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .public_in_list_filter_metadata_param import PublicInListFilterMetadataParam

__all__ = ["PublicInListFilterParam"]


class PublicInListFilterParam(TypedDict, total=False):
    filter_type: Required[Annotated[Literal["IN_LIST"], PropertyInfo(alias="filterType")]]
    """Indicates the type of filter being applied (IN_LIST)."""

    list_id: Required[Annotated[str, PropertyInfo(alias="listId")]]
    """The ID of the list used in the association filter."""

    operator: Required[str]
    """Specifies the operation to be performed by the filter (IN_LIST, NOT_IN_LIST)."""

    metadata: PublicInListFilterMetadataParam
