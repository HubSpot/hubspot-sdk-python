# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicPropertyReferencedTime"]


class PublicPropertyReferencedTime(BaseModel):
    property: str

    reference_type: str = FieldInfo(alias="referenceType")

    time_type: Literal["PROPERTY_REFERENCED"] = FieldInfo(alias="timeType")

    zone_id: str = FieldInfo(alias="zoneId")

    timezone_source: Optional[str] = FieldInfo(alias="timezoneSource", default=None)
