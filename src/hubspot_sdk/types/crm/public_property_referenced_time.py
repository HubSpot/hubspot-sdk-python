# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicPropertyReferencedTime"]


class PublicPropertyReferencedTime(BaseModel):
    property: str
    """Specifies the name of the property that the time reference is applied to."""

    reference_type: str = FieldInfo(alias="referenceType")
    """
    Specifies the type of reference for the property (VALUE, UPDATED_AT,
    ANNIVERSARY, VALUE_WITH_ZONE_SAME_LOCAL_CONVERSION,
    ANNIVERSARY_WITH_ZONE_SAME_LOCAL_CONVERSION).
    """

    time_type: Literal["PROPERTY_REFERENCED"] = FieldInfo(alias="timeType")
    """Defines the type of time (PROPERTY_REFERENCED)."""

    zone_id: str = FieldInfo(alias="zoneId")
    """Indicates the identifier for the time zone associated with the property."""

    timezone_source: Optional[str] = FieldInfo(alias="timezoneSource", default=None)
    """
    Specifies the source of the time zone information for the property (CUSTOM,
    USER, PORTAL).
    """
