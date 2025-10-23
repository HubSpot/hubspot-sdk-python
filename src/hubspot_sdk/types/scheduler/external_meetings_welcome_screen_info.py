# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExternalMeetingsWelcomeScreenInfo"]


class ExternalMeetingsWelcomeScreenInfo(BaseModel):
    description: Optional[str] = None

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)

    show_welcome_screen: Optional[bool] = FieldInfo(alias="showWelcomeScreen", default=None)

    title: Optional[str] = None

    use_company_logo: Optional[bool] = FieldInfo(alias="useCompanyLogo", default=None)
