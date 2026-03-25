# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

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
    """An array containing the closed range availability for a meeting link.

    Closed range times are provided as minute offsets from midnight (e.g., 540
    corresponds to 9am).
    """

    durations: List[int]

    form_fields: List[ExternalLinkFormField] = FieldInfo(alias="formFields")

    legal_consent_enabled: bool = FieldInfo(alias="legalConsentEnabled")
    """Whether the legal consent checkbox is displayed during meeting booking."""

    meeting_buffer_time: int = FieldInfo(alias="meetingBufferTime")
    """The minimum buffer time in milliseconds between consecutive meetings."""

    owner_prioritized: bool = FieldInfo(alias="ownerPrioritized")
    """Indicates whether the meeting owner is prioritized during booking.

    Only applies to link types of ROUND_ROBIN.
    """

    start_time_increment_minutes: Literal[
        "FIFTEEN",
        "FIVE",
        "FORTY_FIVE",
        "MEETING_DURATION",
        "NINETY",
        "ONE_HUNDRED_TWENTY",
        "SIXTY",
        "TEN",
        "THIRTY",
        "TWENTY",
    ] = FieldInfo(alias="startTimeIncrementMinutes")
    """The increment for available start times of meetings, spelt out as a word (e.g.

    15 minute increment corresponds to `FIFTEEN`). `MEETING_DURATION` is also a
    valid value.
    """

    weeks_to_advertise: int = FieldInfo(alias="weeksToAdvertise")
    """
    Legacy property that indicates the number of weeks in advance that availability
    is advertised. May be outdated or superseded by other properties.
    """

    custom_availability_end_date: Optional[int] = FieldInfo(alias="customAvailabilityEndDate", default=None)
    """
    The end date for a meeting link's custom availability window, represented as
    Unix time in milliseconds.
    """

    custom_availability_start_date: Optional[int] = FieldInfo(alias="customAvailabilityStartDate", default=None)
    """
    The start date for a meeting link's custom availability window, represented as
    Unix time in milliseconds.
    """

    display_info: Optional[ExternalLinkDisplayInfo] = FieldInfo(alias="displayInfo", default=None)

    guest_settings: Optional[ExternalGuestSettings] = FieldInfo(alias="guestSettings", default=None)

    language: Optional[str] = None
    """The language setting used for the meeting link."""

    legal_consent_options: Optional[ExternalLegalConsentOptions] = FieldInfo(alias="legalConsentOptions", default=None)

    locale: Optional[str] = None
    """The locale setting used for formatting dates and times in the meeting link."""

    location: Optional[str] = None
    """The physical or virtual location where the meeting will take place."""

    redirect_url: Optional[str] = FieldInfo(alias="redirectUrl", default=None)
    """The URL to redirect to after a meeting is booked."""

    welcome_screen_info: Optional[ExternalMeetingsWelcomeScreenInfo] = FieldInfo(
        alias="welcomeScreenInfo", default=None
    )
