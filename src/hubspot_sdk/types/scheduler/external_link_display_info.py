# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExternalLinkDisplayInfo"]


class ExternalLinkDisplayInfo(BaseModel):
    avatar: Optional[str] = None
    """The URL of the user's custom uploaded avatar image."""

    company_avatar: Optional[str] = FieldInfo(alias="companyAvatar", default=None)
    """The URL of the company's avatar image."""

    headline: Optional[str] = None
    """Deprecated field with no impact of link display info."""

    public_display_avatar_option: Optional[Literal["COMPANY_LOGO", "CUSTOM_AVATAR", "PROFILE_IMAGE"]] = FieldInfo(
        alias="publicDisplayAvatarOption", default=None
    )
    """Option for determining which avatar to display on scheduling page.

    Accepted values are: PROFILE_IMAGE, COMPANY_LOGO, CUSTOM_AVATAR,
    """
