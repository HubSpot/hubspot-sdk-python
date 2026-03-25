# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.property_value import PropertyValue

__all__ = ["MarketingEventDefaultResponse"]


class MarketingEventDefaultResponse(BaseModel):
    custom_properties: List[PropertyValue] = FieldInfo(alias="customProperties")
    """A list of PropertyValues.

    These can be whatever kind of property names and values you want. However, they
    must already exist on the HubSpot account's definition of the MarketingEvent
    Object. If they don't they will be filtered out and not set. In order to do this
    you'll need to create a new PropertyGroup on the HubSpot account's
    MarketingEvent object for your specific app and create the Custom Property you
    want to track on that HubSpot account. Do not create any new default properties
    on the MarketingEvent object as that will apply to all HubSpot accounts.
    """

    event_name: str = FieldInfo(alias="eventName")
    """The name of the marketing event."""

    event_organizer: str = FieldInfo(alias="eventOrganizer")
    """The name of the organizer of the marketing event."""

    end_date_time: Optional[datetime] = FieldInfo(alias="endDateTime", default=None)
    """The end date and time of the marketing event."""

    event_cancelled: Optional[bool] = FieldInfo(alias="eventCancelled", default=None)
    """Indicates if the marketing event has been cancelled."""

    event_completed: Optional[bool] = FieldInfo(alias="eventCompleted", default=None)
    """Indicates if the marketing event has been completed."""

    event_description: Optional[str] = FieldInfo(alias="eventDescription", default=None)
    """The description of the marketing event."""

    event_type: Optional[str] = FieldInfo(alias="eventType", default=None)
    """The type of the marketing event."""

    event_url: Optional[str] = FieldInfo(alias="eventUrl", default=None)
    """
    The URL in the external event application where the marketing event can be
    managed.
    """

    object_id: Optional[str] = FieldInfo(alias="objectId", default=None)
    """The ID of the marketing event CRM object"""

    start_date_time: Optional[datetime] = FieldInfo(alias="startDateTime", default=None)
    """The start date and time of the marketing event."""
