# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExternalLinkDisplayInfo"]


class ExternalLinkDisplayInfo(BaseModel):
    avatar: Optional[str] = None

    company_avatar: Optional[str] = FieldInfo(alias="companyAvatar", default=None)

    headline: Optional[str] = None

    public_display_avatar_option: Optional[str] = FieldInfo(alias="publicDisplayAvatarOption", default=None)
