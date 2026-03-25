# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .external_validated_form_field import ExternalValidatedFormField
from .external_legal_consent_response import ExternalLegalConsentResponse

__all__ = ["ExternalMeetingBookingResponse"]


class ExternalMeetingBookingResponse(BaseModel):
    booking_timezone: str = FieldInfo(alias="bookingTimezone")
    """The timezone the meeting was booked from."""

    calendar_event_id: str = FieldInfo(alias="calendarEventId")
    """The unique identifier for the meeting's calendar event."""

    contact_id: str = FieldInfo(alias="contactId")
    """The ID of the contact associated to the meeting."""

    duration: int
    """The duration of the meeting in milliseconds."""

    end: datetime
    """The date and time when the meeting is scheduled to end, in ISO 8601 format."""

    form_fields: List[ExternalValidatedFormField] = FieldInfo(alias="formFields")

    guest_emails: List[str] = FieldInfo(alias="guestEmails")

    is_offline: bool = FieldInfo(alias="isOffline")
    """
    Whether the meeting was booked offline and no associated calendar event was
    created.
    """

    legal_consent_responses: List[ExternalLegalConsentResponse] = FieldInfo(alias="legalConsentResponses")

    start: datetime
    """The date and time when the meeting is scheduled to start, in ISO 8601 format."""

    subject: str
    """The title of the meeting and calendar event."""

    locale: Optional[str] = None
    """
    The locale the meeting was booked with, used to determine date formatting in
    calendar event description.
    """

    location: Optional[str] = None
    """The physical or virtual location where the meeting will take place."""

    web_conference_meeting_id: Optional[str] = FieldInfo(alias="webConferenceMeetingId", default=None)
    """The unique identifier for the web conference meeting."""

    web_conference_url: Optional[str] = FieldInfo(alias="webConferenceUrl", default=None)
    """The URL for accessing the meeting's web conference."""
