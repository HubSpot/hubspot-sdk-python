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

    calendar_event_id: str = FieldInfo(alias="calendarEventId")

    contact_id: str = FieldInfo(alias="contactId")

    duration: int

    end: datetime

    form_fields: List[ExternalValidatedFormField] = FieldInfo(alias="formFields")

    guest_emails: List[str] = FieldInfo(alias="guestEmails")

    is_offline: bool = FieldInfo(alias="isOffline")

    legal_consent_responses: List[ExternalLegalConsentResponse] = FieldInfo(alias="legalConsentResponses")

    start: datetime

    subject: str

    locale: Optional[str] = None

    location: Optional[str] = None

    web_conference_meeting_id: Optional[str] = FieldInfo(alias="webConferenceMeetingId", default=None)

    web_conference_url: Optional[str] = FieldInfo(alias="webConferenceUrl", default=None)
