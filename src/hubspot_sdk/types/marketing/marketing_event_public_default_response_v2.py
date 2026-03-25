# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .app_info import AppInfo
from ..._models import BaseModel
from .crm_property_wrapper import CrmPropertyWrapper

__all__ = ["MarketingEventPublicDefaultResponseV2"]


class MarketingEventPublicDefaultResponseV2(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")
    """The creation date and time of the marketing event"""

    custom_properties: List[CrmPropertyWrapper] = FieldInfo(alias="customProperties")

    event_name: str = FieldInfo(alias="eventName")
    """The name of the marketing event"""

    object_id: str = FieldInfo(alias="objectId")
    """The internal ID of the marketing event in HubSpot"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The update date and time of the marketing event"""

    app_info: Optional[AppInfo] = FieldInfo(alias="appInfo", default=None)

    end_date_time: Optional[datetime] = FieldInfo(alias="endDateTime", default=None)
    """The end date and time of the marketing event"""

    event_cancelled: Optional[bool] = FieldInfo(alias="eventCancelled", default=None)
    """Indicates if the marketing event has been cancelled"""

    event_completed: Optional[bool] = FieldInfo(alias="eventCompleted", default=None)
    """Indicates if the marketing event has been completed"""

    event_description: Optional[str] = FieldInfo(alias="eventDescription", default=None)
    """The description of the marketing event"""

    event_organizer: Optional[str] = FieldInfo(alias="eventOrganizer", default=None)
    """The name of the organizer of the marketing event"""

    event_type: Optional[str] = FieldInfo(alias="eventType", default=None)
    """The type of the marketing event"""

    event_url: Optional[str] = FieldInfo(alias="eventUrl", default=None)
    """
    A URL in the external event application where the marketing event can be managed
    """

    start_date_time: Optional[datetime] = FieldInfo(alias="startDateTime", default=None)
    """The start date and time of the marketing event"""
