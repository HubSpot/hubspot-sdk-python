# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .external_calendar_meeting_event_response_properties import ExternalCalendarMeetingEventResponseProperties

__all__ = ["ExternalCalenderMeetingEventResponse"]


class ExternalCalenderMeetingEventResponse(BaseModel):
    id: str
    """The unique identifier for the meeting event."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """
    The date and time when the meeting event was initially created, in ISO 8601
    format.
    """

    last_updated_at: datetime = FieldInfo(alias="lastUpdatedAt")
    """The date and time when the meeting event was last updated, in ISO 8601 format."""

    properties: ExternalCalendarMeetingEventResponseProperties
