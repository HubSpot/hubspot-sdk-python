# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExternalMeetingAvailability"]


class ExternalMeetingAvailability(BaseModel):
    end_millis_utc: int = FieldInfo(alias="endMillisUtc")
    """
    The end time of the meeting availability, represented as Unix time in
    milliseconds.
    """

    start_millis_utc: int = FieldInfo(alias="startMillisUtc")
    """
    The start time of the meeting availability, represented as Unix time in
    milliseconds.
    """
