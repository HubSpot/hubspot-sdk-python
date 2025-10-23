# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .external_user_busy_times import ExternalUserBusyTimes
from .external_branding_metadata import ExternalBrandingMetadata
from .external_link_availability import ExternalLinkAvailability
from .external_meetings_link_settings import ExternalMeetingsLinkSettings

__all__ = ["ExternalBookingInfo"]


class ExternalBookingInfo(BaseModel):
    all_users_busy_times: List[ExternalUserBusyTimes] = FieldInfo(alias="allUsersBusyTimes")

    custom_params: ExternalMeetingsLinkSettings = FieldInfo(alias="customParams")

    is_offline: bool = FieldInfo(alias="isOffline")

    link_id: str = FieldInfo(alias="linkId")

    link_type: Literal["PERSONAL_LINK", "GROUP_CALENDAR", "ROUND_ROBIN_CALENDAR"] = FieldInfo(alias="linkType")

    branding_metadata: Optional[ExternalBrandingMetadata] = FieldInfo(alias="brandingMetadata", default=None)

    link_availability: Optional[ExternalLinkAvailability] = FieldInfo(alias="linkAvailability", default=None)
