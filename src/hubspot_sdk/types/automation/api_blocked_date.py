# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIBlockedDate"]


class APIBlockedDate(BaseModel):
    day_of_month: int = FieldInfo(alias="dayOfMonth")

    month: Literal[
        "APRIL",
        "AUGUST",
        "DECEMBER",
        "FEBRUARY",
        "JANUARY",
        "JULY",
        "JUNE",
        "MARCH",
        "MAY",
        "NOVEMBER",
        "OCTOBER",
        "SEPTEMBER",
    ]

    year: Optional[int] = None
