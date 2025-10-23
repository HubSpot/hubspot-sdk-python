# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExternalMeetingAvailability"]


class ExternalMeetingAvailability(BaseModel):
    end_millis_utc: int = FieldInfo(alias="endMillisUtc")

    start_millis_utc: int = FieldInfo(alias="startMillisUtc")
