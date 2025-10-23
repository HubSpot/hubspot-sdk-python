# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .unenrollment_settings_response import UnenrollmentSettingsResponse

__all__ = ["PublicSequenceSettingsResponse"]


class PublicSequenceSettingsResponse(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    eligible_follow_up_days: str = FieldInfo(alias="eligibleFollowUpDays")

    individual_task_reminders_enabled: bool = FieldInfo(alias="individualTaskRemindersEnabled")

    selling_strategy: str = FieldInfo(alias="sellingStrategy")

    send_window_end_minute: int = FieldInfo(alias="sendWindowEndMinute")

    send_window_start_minute: int = FieldInfo(alias="sendWindowStartMinute")

    task_reminder_minute: int = FieldInfo(alias="taskReminderMinute")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    unenrollment_settings: Optional[UnenrollmentSettingsResponse] = FieldInfo(
        alias="unenrollmentSettings", default=None
    )
