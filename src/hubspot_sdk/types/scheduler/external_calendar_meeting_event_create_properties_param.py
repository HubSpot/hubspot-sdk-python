# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ExternalCalendarMeetingEventCreatePropertiesParam"]


class ExternalCalendarMeetingEventCreatePropertiesParam(TypedDict, total=False):
    hs_meeting_end_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    hs_meeting_outcome: Required[str]

    hs_meeting_start_time: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    hs_meeting_title: Required[str]

    hs_timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    hs_activity_type: str

    hs_attachment_ids: SequenceNotStr[str]

    hs_attendee_owner_ids: SequenceNotStr[str]

    hs_internal_meeting_notes: str

    hs_meeting_body: str

    hs_meeting_location: str

    hs_meeting_location_type: str

    hubspot_owner_id: str
