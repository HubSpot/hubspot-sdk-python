# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicSequenceSettingsResponse"]


class PublicSequenceSettingsResponse(BaseModel):
    id: str
    """The unique identifier for the sequence settings."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp of when the sequence settings were created."""

    eligible_follow_up_days: Literal["BUSINESS_DAYS", "EVERYDAY", "WEEKDAYS_ONLY"] = FieldInfo(
        alias="eligibleFollowUpDays"
    )
    """Specifies the days on which follow-up actions are allowed."""

    individual_task_reminders_enabled: bool = FieldInfo(alias="individualTaskRemindersEnabled")
    """Indicates whether individual task reminders are enabled."""

    selling_strategy: Literal["ACCOUNT_BASED", "LEAD_BASED"] = FieldInfo(alias="sellingStrategy")
    """
    (deprecated) Defines the unenrollment strategy, with accepted values being
    ACCOUNT_BASED or LEAD_BASED. If ACCOUNT_BASED is used, all contacts associated
    with the same company will be unenrolled if one contact meets any of the
    unenrollment criteria.
    """

    send_window_end_minute: int = FieldInfo(alias="sendWindowEndMinute")
    """
    Indicates the end minute of the time window during which automated emails can be
    sent.
    """

    send_window_start_minute: int = FieldInfo(alias="sendWindowStartMinute")
    """
    Indicates the start minute of the time window during which automated emails can
    be sent.
    """

    task_reminder_minute: int = FieldInfo(alias="taskReminderMinute")
    """Specifies the minute of day at which task reminders are triggered."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The timestamp of when the sequence settings were last updated."""
