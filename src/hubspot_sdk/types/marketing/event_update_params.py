# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .property_value_param import PropertyValueParam

__all__ = ["EventUpdateParams"]


class EventUpdateParams(TypedDict, total=False):
    custom_properties: Required[Annotated[Iterable[PropertyValueParam], PropertyInfo(alias="customProperties")]]

    end_date_time: Annotated[Union[str, datetime], PropertyInfo(alias="endDateTime", format="iso8601")]

    event_cancelled: Annotated[bool, PropertyInfo(alias="eventCancelled")]

    event_description: Annotated[str, PropertyInfo(alias="eventDescription")]

    event_name: Annotated[str, PropertyInfo(alias="eventName")]

    event_organizer: Annotated[str, PropertyInfo(alias="eventOrganizer")]

    event_type: Annotated[str, PropertyInfo(alias="eventType")]

    event_url: Annotated[str, PropertyInfo(alias="eventUrl")]

    start_date_time: Annotated[Union[str, datetime], PropertyInfo(alias="startDateTime", format="iso8601")]
