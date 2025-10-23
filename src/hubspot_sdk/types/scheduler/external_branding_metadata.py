# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExternalBrandingMetadata"]


class ExternalBrandingMetadata(BaseModel):
    logo_alt_text: str = FieldInfo(alias="logoAltText")

    show_marketing_ad: bool = FieldInfo(alias="showMarketingAd")

    show_sales_ad: bool = FieldInfo(alias="showSalesAd")

    accent2_color: Optional[str] = FieldInfo(alias="accent2Color", default=None)

    accent_color: Optional[str] = FieldInfo(alias="accentColor", default=None)

    company_address_line1: Optional[str] = FieldInfo(alias="companyAddressLine1", default=None)

    company_address_line2: Optional[str] = FieldInfo(alias="companyAddressLine2", default=None)

    company_avatar: Optional[str] = FieldInfo(alias="companyAvatar", default=None)

    company_city: Optional[str] = FieldInfo(alias="companyCity", default=None)

    company_country: Optional[str] = FieldInfo(alias="companyCountry", default=None)

    company_domain: Optional[str] = FieldInfo(alias="companyDomain", default=None)

    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)

    company_state: Optional[str] = FieldInfo(alias="companyState", default=None)

    company_zip: Optional[str] = FieldInfo(alias="companyZip", default=None)

    logo_height: Optional[int] = FieldInfo(alias="logoHeight", default=None)

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)

    logo_width: Optional[int] = FieldInfo(alias="logoWidth", default=None)

    primary_color: Optional[str] = FieldInfo(alias="primaryColor", default=None)

    secondary_color: Optional[str] = FieldInfo(alias="secondaryColor", default=None)
