# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PropertyReferencedTime"]


class PropertyReferencedTime(BaseModel):
    property: str

    reference_type: Literal[
        "VALUE",
        "UPDATED_AT",
        "ANNIVERSARY",
        "VALUE_WITH_ZONE_SAME_LOCAL_CONVERSION",
        "ANNIVERSARY_WITH_ZONE_SAME_LOCAL_CONVERSION",
    ] = FieldInfo(alias="referenceType")

    time_type: Literal["PROPERTY_REFERENCED"] = FieldInfo(alias="timeType")

    timezone_source: Literal["CUSTOM", "USER", "PORTAL"] = FieldInfo(alias="timezoneSource")

    zone_id: str = FieldInfo(alias="zoneId")
