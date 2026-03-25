# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DateTime"]


class DateTime(BaseModel):
    date_only: bool = FieldInfo(alias="dateOnly")
    """
    Indicates whether the DateTime value represents only a date without a time
    component.
    """

    time_zone_shift: int = FieldInfo(alias="timeZoneShift")
    """
    The integer value representing the shift in minutes from UTC for the DateTime
    value.
    """

    value: int
    """The integer value representing a specific point in time."""
