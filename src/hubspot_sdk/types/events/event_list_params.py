# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["EventListParams", "ObjectProperty", "Property"]


class EventListParams(TypedDict, total=False):
    id: SequenceNotStr[str]
    """ID of an event instance.

    IDs are 1:1 with event instances. If you provide this filter and additional
    filters, the other filters must match the values on the event instance to yield
    results.
    """

    after: str
    """
    The paging cursor token of the last successfully read resource will be returned
    as the `paging.next.after` JSON property of a paged response containing more
    results.
    """

    before: str
    """Pagination cursor for backward navigation.

    Retrieves events occurring before the specified cursor position. Note: Currently
    only forward pagination with after is supported.
    """

    event_type: Annotated[str, PropertyInfo(alias="eventType")]
    """The event type name.

    You can retrieve available event types using the
    [event types endpoint](#get-%2Fevents%2Fv3%2Fevents%2Fevent-types).
    """

    limit: int
    """The maximum number of results to display per page."""

    object_id: Annotated[int, PropertyInfo(alias="objectId")]
    """The ID of the CRM Object to filter event instances on.

    When including this parameter, you must also include the `objectType` parameter.
    """

    object_property: Annotated[ObjectProperty, PropertyInfo(alias="objectProperty")]

    object_type: Annotated[str, PropertyInfo(alias="objectType")]
    """The type of CRM object to filter event instances on (e.g., `contact`).

    To retrieve event data for a specific CRM record, include the additional
    `objectId` query parameter (below).
    """

    occurred_after: Annotated[Union[str, datetime], PropertyInfo(alias="occurredAfter", format="iso8601")]
    """Filter for event data that occurred after a specific datetime."""

    occurred_before: Annotated[Union[str, datetime], PropertyInfo(alias="occurredBefore", format="iso8601")]
    """Filter for event data that occurred before a specific datetime."""

    property: Property

    sort: SequenceNotStr[str]
    """
    Sort direction based on the timestamp of the event instance, `ASCENDING` or
    `DESCENDING`.
    """


class ObjectProperty(TypedDict, total=False):
    propname: Annotated[object, PropertyInfo(alias="{propname}")]
    """
    Instead of retrieving event data for a specific object by its ID, you can
    specify a unique identifier property. For contacts, you can use the `email`
    property. (e.g., `objectProperty.email=name@domain.com`).
    """


class Property(TypedDict, total=False):
    propname: Annotated[object, PropertyInfo(alias="{propname}")]
    """
    Filter for event completions that contain a specific value for an event property
    (e.g., `property.hs_city=portland`). For properties values with spaces, replaces
    spaces with `%20` or `+` (e.g., `property.hs_city=new+york`).
    """
