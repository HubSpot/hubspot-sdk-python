# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .external_user_busy_times import ExternalUserBusyTimes
from .external_link_availability import ExternalLinkAvailability

__all__ = ["ExternalLinkAvailabilityAndBusyTimes"]


class ExternalLinkAvailabilityAndBusyTimes(BaseModel):
    all_users_busy_times: List[ExternalUserBusyTimes] = FieldInfo(alias="allUsersBusyTimes")

    link_availability: Optional[ExternalLinkAvailability] = FieldInfo(alias="linkAvailability", default=None)
