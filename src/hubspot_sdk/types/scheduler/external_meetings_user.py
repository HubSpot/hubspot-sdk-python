# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .external_user_profile import ExternalUserProfile

__all__ = ["ExternalMeetingsUser"]


class ExternalMeetingsUser(BaseModel):
    id: str
    """The ID for the meetings user. This value is different than the userId."""

    calendar_provider: Literal["EXCHANGE", "GOOGLE", "OFFICE365", "UNKNOWN"] = FieldInfo(alias="calendarProvider")
    """The calendar provider associated with the user.

    Accepted values are: GOOGLE, OFFICE365, EXCHANGE, UNKNOWN.
    """

    is_sales_starter: bool = FieldInfo(alias="isSalesStarter")
    """Whether the user has a sales starter seat."""

    user_id: str = FieldInfo(alias="userId")
    """The ID of the user."""

    user_profile: ExternalUserProfile = FieldInfo(alias="userProfile")
