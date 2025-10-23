# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .external_user_profile import ExternalUserProfile

__all__ = ["ExternalMeetingsUser"]


class ExternalMeetingsUser(BaseModel):
    id: str

    calendar_provider: str = FieldInfo(alias="calendarProvider")

    is_sales_starter: bool = FieldInfo(alias="isSalesStarter")

    user_id: str = FieldInfo(alias="userId")

    user_profile: ExternalUserProfile = FieldInfo(alias="userProfile")
