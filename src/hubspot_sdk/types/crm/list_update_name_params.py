# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ListUpdateNameParams"]


class ListUpdateNameParams(TypedDict, total=False):
    include_filters: Annotated[bool, PropertyInfo(alias="includeFilters")]
    """
    A flag indicating whether or not the response object list definition should
    include a filter branch definition. By default, object list definitions will not
    have their filter branch definitions included in the response.
    """

    list_name: Annotated[str, PropertyInfo(alias="listName")]
    """The name to update the list to."""
