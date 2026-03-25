# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.property_value import PropertyValue

__all__ = ["EventCreateParams"]


class EventCreateParams(TypedDict, total=False):
    custom_properties: Required[Annotated[Iterable[PropertyValue], PropertyInfo(alias="customProperties")]]
    """A list of PropertyValues.

    These can be whatever kind of property names and values you want. However, they
    must already exist on the HubSpot account's definition of the MarketingEvent
    Object. If they don't they will be filtered out and not set. In order to do this
    you'll need to create a new PropertyGroup on the HubSpot account's
    MarketingEvent object for your specific app and create the Custom Property you
    want to track on that HubSpot account. Do not create any new default properties
    on the MarketingEvent object as that will apply to all HubSpot accounts.
    """

    event_name: Required[Annotated[str, PropertyInfo(alias="eventName")]]
    """The name of the marketing event."""

    event_organizer: Required[Annotated[str, PropertyInfo(alias="eventOrganizer")]]
    """The name of the organizer of the marketing event."""

    external_account_id: Required[Annotated[str, PropertyInfo(alias="externalAccountId")]]
    """
    The accountId that is associated with this marketing event in the external event
    application.
    """

    external_event_id: Required[Annotated[str, PropertyInfo(alias="externalEventId")]]
    """The id of the marketing event in the external event application."""

    end_date_time: Annotated[Union[str, datetime], PropertyInfo(alias="endDateTime", format="iso8601")]
    """The end date and time of the marketing event."""

    event_cancelled: Annotated[bool, PropertyInfo(alias="eventCancelled")]
    """Indicates if the marketing event has been cancelled. Defaults to `false`"""

    event_completed: Annotated[bool, PropertyInfo(alias="eventCompleted")]
    """Indicates if the marketing event has been completed. Defaults to `false`"""

    event_description: Annotated[str, PropertyInfo(alias="eventDescription")]
    """The description of the marketing event."""

    event_type: Annotated[str, PropertyInfo(alias="eventType")]
    """Describes what type of event this is.

    For example: `WEBINAR`, `CONFERENCE`, `WORKSHOP`
    """

    event_url: Annotated[str, PropertyInfo(alias="eventUrl")]
    """
    A URL in the external event application where the marketing event can be
    managed.
    """

    start_date_time: Annotated[Union[str, datetime], PropertyInfo(alias="startDateTime", format="iso8601")]
    """The start date and time of the marketing event."""
