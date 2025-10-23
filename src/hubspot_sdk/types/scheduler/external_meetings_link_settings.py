# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .external_closed_range import ExternalClosedRange
from .external_guest_settings import ExternalGuestSettings
from .external_link_form_field import ExternalLinkFormField
from .external_link_display_info import ExternalLinkDisplayInfo
from .external_legal_consent_options import ExternalLegalConsentOptions
from .external_meetings_welcome_screen_info import ExternalMeetingsWelcomeScreenInfo

__all__ = ["ExternalMeetingsLinkSettings"]


class ExternalMeetingsLinkSettings(BaseModel):
    availability: Dict[str, ExternalClosedRange]

    durations: List[int]

    form_fields: List[ExternalLinkFormField] = FieldInfo(alias="formFields")

    legal_consent_enabled: bool = FieldInfo(alias="legalConsentEnabled")

    meeting_buffer_time: int = FieldInfo(alias="meetingBufferTime")

    owner_prioritized: bool = FieldInfo(alias="ownerPrioritized")

    start_time_increment_minutes: str = FieldInfo(alias="startTimeIncrementMinutes")

    weeks_to_advertise: int = FieldInfo(alias="weeksToAdvertise")

    custom_availability_end_date: Optional[int] = FieldInfo(alias="customAvailabilityEndDate", default=None)

    custom_availability_start_date: Optional[int] = FieldInfo(alias="customAvailabilityStartDate", default=None)

    display_info: Optional[ExternalLinkDisplayInfo] = FieldInfo(alias="displayInfo", default=None)

    guest_settings: Optional[ExternalGuestSettings] = FieldInfo(alias="guestSettings", default=None)

    language: Optional[str] = None

    legal_consent_options: Optional[ExternalLegalConsentOptions] = FieldInfo(alias="legalConsentOptions", default=None)

    locale: Optional[str] = None

    location: Optional[str] = None

    redirect_url: Optional[str] = FieldInfo(alias="redirectUrl", default=None)

    welcome_screen_info: Optional[ExternalMeetingsWelcomeScreenInfo] = FieldInfo(
        alias="welcomeScreenInfo", default=None
    )
