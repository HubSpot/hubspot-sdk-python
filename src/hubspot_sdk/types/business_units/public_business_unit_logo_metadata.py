# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicBusinessUnitLogoMetadata"]


class PublicBusinessUnitLogoMetadata(BaseModel):
    logo_alt_text: Optional[str] = FieldInfo(alias="logoAltText", default=None)
    """The logo's alt text"""

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """The logo's url"""

    resized_url: Optional[str] = FieldInfo(alias="resizedUrl", default=None)
    """The logo's resized url"""
