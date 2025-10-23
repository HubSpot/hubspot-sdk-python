# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .app_info import AppInfo
from ..._models import BaseModel
from .crm_property_wrapper import CRMPropertyWrapper

__all__ = ["MarketingEventPublicReadResponseV2"]


class MarketingEventPublicReadResponseV2(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    custom_properties: List[CRMPropertyWrapper] = FieldInfo(alias="customProperties")

    event_name: str = FieldInfo(alias="eventName")

    object_id: str = FieldInfo(alias="objectId")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    app_info: Optional[AppInfo] = FieldInfo(alias="appInfo", default=None)

    attendees: Optional[int] = None

    cancellations: Optional[int] = None

    end_date_time: Optional[datetime] = FieldInfo(alias="endDateTime", default=None)

    event_cancelled: Optional[bool] = FieldInfo(alias="eventCancelled", default=None)

    event_completed: Optional[bool] = FieldInfo(alias="eventCompleted", default=None)

    event_description: Optional[str] = FieldInfo(alias="eventDescription", default=None)

    event_organizer: Optional[str] = FieldInfo(alias="eventOrganizer", default=None)

    event_status: Optional[str] = FieldInfo(alias="eventStatus", default=None)

    event_type: Optional[str] = FieldInfo(alias="eventType", default=None)

    event_url: Optional[str] = FieldInfo(alias="eventUrl", default=None)

    external_event_id: Optional[str] = FieldInfo(alias="externalEventId", default=None)

    no_shows: Optional[int] = FieldInfo(alias="noShows", default=None)

    registrants: Optional[int] = None

    start_date_time: Optional[datetime] = FieldInfo(alias="startDateTime", default=None)
