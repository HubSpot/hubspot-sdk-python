# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .external_reminder_param import ExternalReminderParam

__all__ = ["ExternalEmailReminderScheduleParam"]


class ExternalEmailReminderScheduleParam(TypedDict, total=False):
    reminders: Required[Iterable[ExternalReminderParam]]

    should_include_invite_description: Required[Annotated[bool, PropertyInfo(alias="shouldIncludeInviteDescription")]]
