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
    """An array of event IDs to filter by."""

    after: str
    """A cursor token for pagination.

    Use the value from the previous response's paging.next.after field.
    """

    before: str
    """A cursor token to retrieve results before a specific point."""

    event_type: Annotated[str, PropertyInfo(alias="eventType")]
    """The type of event to filter by."""

    limit: int
    """The maximum number of results to display per page."""

    object_id: Annotated[int, PropertyInfo(alias="objectId")]
    """The unique identifier of the object associated with the events."""

    object_property: Annotated[ObjectProperty, PropertyInfo(alias="objectProperty")]

    object_type: Annotated[str, PropertyInfo(alias="objectType")]
    """The type of object associated with the events."""

    occurred_after: Annotated[Union[str, datetime], PropertyInfo(alias="occurredAfter", format="iso8601")]
    """Filter events that occurred after this date-time."""

    occurred_before: Annotated[Union[str, datetime], PropertyInfo(alias="occurredBefore", format="iso8601")]
    """Filter events that occurred before this date-time."""

    properties: SequenceNotStr[str]
    """An array of property names to include in the response."""

    property: Property

    sort: SequenceNotStr[str]
    """An array of fields to sort the results by."""


class ObjectProperty(TypedDict, total=False):
    propname: Annotated[object, PropertyInfo(alias="{propname}")]
    """Filter events by specific object properties."""


class Property(TypedDict, total=False):
    propname: Annotated[object, PropertyInfo(alias="{propname}")]
    """Filter events by specific event properties."""
