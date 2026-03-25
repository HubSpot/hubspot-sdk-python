# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo
from ..filter_group_param import FilterGroupParam

__all__ = ["CartSearchParams"]


class CartSearchParams(TypedDict, total=False):
    after: Required[str]
    """A paging cursor token for retrieving subsequent pages."""

    filter_groups: Required[Annotated[Iterable[FilterGroupParam], PropertyInfo(alias="filterGroups")]]
    """Up to 6 groups of filters defining additional query criteria."""

    limit: Required[int]
    """The maximum results to return, up to 200 objects."""

    properties: Required[SequenceNotStr[str]]
    """A list of property names to include in the response."""

    sorts: Required[SequenceNotStr[str]]
    """Specifies sorting order based on object properties."""

    query: str
    """The search query string, up to 3000 characters."""
