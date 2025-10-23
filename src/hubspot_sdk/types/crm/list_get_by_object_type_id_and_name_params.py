# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ListGetByObjectTypeIDAndNameParams"]


class ListGetByObjectTypeIDAndNameParams(TypedDict, total=False):
    object_type_id: Required[Annotated[str, PropertyInfo(alias="objectTypeId")]]

    include_filters: Annotated[bool, PropertyInfo(alias="includeFilters")]
    """
    A flag indicating whether or not the response object list definition should
    include a filter branch definition. By default, object list definitions will not
    have their filter branch definitions included in the response.
    """
