# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIStaticTimeZoneStrategy"]


class APIStaticTimeZoneStrategy(BaseModel):
    time_zone_id: str = FieldInfo(alias="timeZoneId")

    type: Literal["STATIC_TIME_ZONE"]
