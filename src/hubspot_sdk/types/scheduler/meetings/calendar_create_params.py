# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..external_email_reminder_schedule_param import ExternalEmailReminderScheduleParam
from ..external_association_create_request_param import ExternalAssociationCreateRequestParam
from ..external_calendar_meeting_event_create_properties_param import ExternalCalendarMeetingEventCreatePropertiesParam

__all__ = ["CalendarCreateParams"]


class CalendarCreateParams(TypedDict, total=False):
    associations: Required[Iterable[ExternalAssociationCreateRequestParam]]

    email_reminder_schedule: Required[
        Annotated[ExternalEmailReminderScheduleParam, PropertyInfo(alias="emailReminderSchedule")]
    ]

    properties: Required[ExternalCalendarMeetingEventCreatePropertiesParam]

    timezone: Required[str]
