# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["OccurrenceListParams", "ObjectProperty", "Property"]


class OccurrenceListParams(TypedDict, total=False):
    id: SequenceNotStr[str]

    after: str
    """
    The paging cursor token of the last successfully read resource will be returned
    as the `paging.next.after` JSON property of a paged response containing more
    results.
    """

    before: str

    event_type: Annotated[str, PropertyInfo(alias="eventType")]

    limit: int
    """The maximum number of results to display per page."""

    object_id: Annotated[int, PropertyInfo(alias="objectId")]

    object_property: Annotated[ObjectProperty, PropertyInfo(alias="objectProperty")]

    object_type: Annotated[str, PropertyInfo(alias="objectType")]

    occurred_after: Annotated[Union[str, datetime], PropertyInfo(alias="occurredAfter", format="iso8601")]

    occurred_before: Annotated[Union[str, datetime], PropertyInfo(alias="occurredBefore", format="iso8601")]

    properties: SequenceNotStr[str]

    property: Property

    sort: SequenceNotStr[str]


class ObjectProperty(TypedDict, total=False):
    propname: Annotated[object, PropertyInfo(alias="{propname}")]


class Property(TypedDict, total=False):
    propname: Annotated[object, PropertyInfo(alias="{propname}")]
