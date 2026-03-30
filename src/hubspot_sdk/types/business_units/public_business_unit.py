# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_business_unit_logo_metadata import PublicBusinessUnitLogoMetadata

__all__ = ["PublicBusinessUnit"]


class PublicBusinessUnit(BaseModel):
    id: str
    """The Business Unit's unique ID"""

    name: str
    """The Business Unit's name"""

    logo_metadata: Optional[PublicBusinessUnitLogoMetadata] = FieldInfo(alias="logoMetadata", default=None)
