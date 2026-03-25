# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.property_value import PropertyValue

__all__ = ["MarketingEventPublicUpdateRequestFullV2Param"]


class MarketingEventPublicUpdateRequestFullV2Param(TypedDict, total=False):
    custom_properties: Required[Annotated[Iterable[PropertyValue], PropertyInfo(alias="customProperties")]]

    object_id: Required[Annotated[str, PropertyInfo(alias="objectId")]]
    """The internal ID of the marketing event in HubSpot"""

    end_date_time: Annotated[Union[str, datetime], PropertyInfo(alias="endDateTime", format="iso8601")]
    """The end date and time of the marketing event"""

    event_cancelled: Annotated[bool, PropertyInfo(alias="eventCancelled")]
    """Indicates if the marketing event has been cancelled"""

    event_description: Annotated[str, PropertyInfo(alias="eventDescription")]
    """The description of the marketing event"""

    event_name: Annotated[str, PropertyInfo(alias="eventName")]
    """The name of the marketing event"""

    event_organizer: Annotated[str, PropertyInfo(alias="eventOrganizer")]
    """The name of the organizer of the marketing event"""

    event_type: Annotated[str, PropertyInfo(alias="eventType")]
    """The type of the marketing event"""

    event_url: Annotated[str, PropertyInfo(alias="eventUrl")]
    """
    A URL in the external event application where the marketing event can be managed
    """

    start_date_time: Annotated[Union[str, datetime], PropertyInfo(alias="startDateTime", format="iso8601")]
    """The start date and time of the marketing event"""
