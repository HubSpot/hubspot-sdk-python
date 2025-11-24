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

    reference_type: Literal["WEEK"] = FieldInfo(alias="referenceType")

    hour: Optional[int] = None

    millisecond: Optional[int] = None

    minute: Optional[int] = None

    second: Optional[int] = None
