# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .email_settings_response import EmailSettingsResponse
from .meeting_settings_response import MeetingSettingsResponse

__all__ = ["UnenrollmentSettingsResponse"]


class UnenrollmentSettingsResponse(BaseModel):
    email_settings: EmailSettingsResponse = FieldInfo(alias="emailSettings")

    meeting_settings: MeetingSettingsResponse = FieldInfo(alias="meetingSettings")
