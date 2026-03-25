# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExternalBrandingMetadata"]


class ExternalBrandingMetadata(BaseModel):
    logo_alt_text: str = FieldInfo(alias="logoAltText")
    """The alternative text for the current logo."""

    show_marketing_ad: bool = FieldInfo(alias="showMarketingAd")
    """Whether Hubspot Marketing ads are shown."""

    show_sales_ad: bool = FieldInfo(alias="showSalesAd")
    """Whether Hubspot Sales ads are shown."""

    accent2_color: Optional[str] = FieldInfo(alias="accent2Color", default=None)
    """The secondary accent color used in branding."""

    accent_color: Optional[str] = FieldInfo(alias="accentColor", default=None)
    """The primary accent color used in branding."""

    company_address_line1: Optional[str] = FieldInfo(alias="companyAddressLine1", default=None)
    """The first line of the company's address."""

    company_address_line2: Optional[str] = FieldInfo(alias="companyAddressLine2", default=None)
    """The second line of the company's address."""

    company_avatar: Optional[str] = FieldInfo(alias="companyAvatar", default=None)
    """The URL of the company's avatar image."""

    company_city: Optional[str] = FieldInfo(alias="companyCity", default=None)
    """The city where the company is located."""

    company_country: Optional[str] = FieldInfo(alias="companyCountry", default=None)
    """The country where the company is located."""

    company_domain: Optional[str] = FieldInfo(alias="companyDomain", default=None)
    """The domain of the company's website."""

    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)
    """The name of the company."""

    company_state: Optional[str] = FieldInfo(alias="companyState", default=None)
    """The state where the company is located."""

    company_zip: Optional[str] = FieldInfo(alias="companyZip", default=None)
    """The ZIP code of the company's location."""

    logo_height: Optional[int] = FieldInfo(alias="logoHeight", default=None)
    """The height of the logo in pixels."""

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """The URL of a custom logo image."""

    logo_width: Optional[int] = FieldInfo(alias="logoWidth", default=None)
    """The width of the logo in pixels."""

    primary_color: Optional[str] = FieldInfo(alias="primaryColor", default=None)
    """The primary color used in branding."""

    secondary_color: Optional[str] = FieldInfo(alias="secondaryColor", default=None)
    """The secondary color used in branding."""
