# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .external_meeting_availability import ExternalMeetingAvailability

__all__ = ["ExternalLinkAvailabilityForDuration"]


class ExternalLinkAvailabilityForDuration(BaseModel):
    availabilities: List[ExternalMeetingAvailability]

    meeting_duration_millis: int = FieldInfo(alias="meetingDurationMillis")
