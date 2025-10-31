# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIStaticDateAnchor"]


class APIStaticDateAnchor(BaseModel):
    day_of_month: int = FieldInfo(alias="dayOfMonth")

    month: Literal[
        "JANUARY",
        "FEBRUARY",
        "MARCH",
        "APRIL",
        "MAY",
        "JUNE",
        "JULY",
        "AUGUST",
        "SEPTEMBER",
        "OCTOBER",
        "NOVEMBER",
        "DECEMBER",
    ]

    type: Literal["STATIC_DATE_ANCHOR"]

    year: Optional[int] = None
