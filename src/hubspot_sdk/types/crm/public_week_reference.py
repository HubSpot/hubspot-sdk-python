# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicWeekReference"]


class PublicWeekReference(BaseModel):
    day_of_week: Literal["FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"] = FieldInfo(
        alias="dayOfWeek"
    )
    """
    The day of the week (SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY,
    SATURDAY).
    """

    reference_type: Literal["WEEK"] = FieldInfo(alias="referenceType")
    """Indicates the type of reference (WEEK)."""

    hour: Optional[int] = None
    """The hour component of the week reference."""

    millisecond: Optional[int] = None
    """The millisecond component of the week reference."""

    minute: Optional[int] = None
    """The minute component of the week reference."""

    second: Optional[int] = None
    """The second component of the week reference."""
