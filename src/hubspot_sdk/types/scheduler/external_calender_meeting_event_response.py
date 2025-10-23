# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .external_calendar_meeting_event_response_properties import ExternalCalendarMeetingEventResponseProperties

__all__ = ["ExternalCalenderMeetingEventResponse"]


class ExternalCalenderMeetingEventResponse(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    last_updated_at: datetime = FieldInfo(alias="lastUpdatedAt")

    properties: ExternalCalendarMeetingEventResponseProperties
