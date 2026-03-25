# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExternalMeetingsWelcomeScreenInfo"]


class ExternalMeetingsWelcomeScreenInfo(BaseModel):
    description: Optional[str] = None
    """A brief description displayed the welcome screen below the title."""

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """
    The URL of the logo image to be displayed on the welcome screen, only used if
    `useCompanyLogo` is false.
    """

    show_welcome_screen: Optional[bool] = FieldInfo(alias="showWelcomeScreen", default=None)
    """Deprecated property. Value can be ignored but will always be false."""

    title: Optional[str] = None
    """The main heading displayed on the welcome screen."""

    use_company_logo: Optional[bool] = FieldInfo(alias="useCompanyLogo", default=None)
    """Whether the company's logo should be displayed on the welcome screen."""
