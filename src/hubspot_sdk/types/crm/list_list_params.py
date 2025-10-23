# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ListListParams"]


class ListListParams(TypedDict, total=False):
    include_filters: Annotated[bool, PropertyInfo(alias="includeFilters")]
    """
    A flag indicating whether or not the response object list definitions should
    include a filter branch definition. By default, object list definitions will not
    have their filter branch definitions included in the response.
    """

    list_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="listIds")]
    """The **ILS IDs** of the lists to fetch."""
