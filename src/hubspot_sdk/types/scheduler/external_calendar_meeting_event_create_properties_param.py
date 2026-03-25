# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ExternalCalendarMeetingEventCreatePropertiesParam"]


class ExternalCalendarMeetingEventCreatePropertiesParam(TypedDict, total=False):
    hs_meeting_end_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The time that the meeting should end in ISO 8601 format."""

    hs_meeting_outcome: Required[str]
    """The outcome of the meeting.

    Acceptable default values are: SCHEDULED, COMPLETED, RESCHEDULED, NO_SHOW,
    CANCELED. This property can be changed to include additional custom values.
    """

    hs_meeting_start_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The time that the meeting should start in ISO 8601 format."""

    hs_meeting_title: Required[str]
    """The title of the meeting and calendar event."""

    hs_timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The time that the meeting should start in ISO 8601 format.

    This value should be the same as `hs_meeting_start_time`.
    """

    hubspot_owner_id: Required[str]
    """The ownerId of the HubSpot user who will host the meeting."""

    hs_activity_type: str
    """The activity type of the meeting.

    Acceptable values are based on portal defined call and meeting types.
    """

    hs_attachment_ids: SequenceNotStr[str]

    hs_attendee_owner_ids: SequenceNotStr[str]

    hs_internal_meeting_notes: str
    """Internal notes related to the meeting."""

    hs_meeting_body: str
    """The description of the meeting and calendar event."""

    hs_meeting_location: str
    """
    The physical address, virtual location, or phone number where the meeting will
    take place.
    """

    hs_meeting_location_type: Literal["ADDRESS", "CUSTOM", "PHONE"]
    """The type of location for the meeting.

    Acceptable values are: ADDRESS, CUSTOM, PHONE.
    """
