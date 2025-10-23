# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .external_time_range import ExternalTimeRange
from .external_meetings_user import ExternalMeetingsUser

__all__ = ["ExternalUserBusyTimes"]


class ExternalUserBusyTimes(BaseModel):
    busy_times: List[ExternalTimeRange] = FieldInfo(alias="busyTimes")

    is_offline: bool = FieldInfo(alias="isOffline")

    meetings_user: ExternalMeetingsUser = FieldInfo(alias="meetingsUser")
