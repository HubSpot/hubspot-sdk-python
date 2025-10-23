# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIStaticDateAnchor"]


class APIStaticDateAnchor(BaseModel):
    day_of_month: int = FieldInfo(alias="dayOfMonth")
    """The day of the date to anchor on"""

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
    """The month of the date to anchor on"""

    type: Literal["STATIC_DATE_ANCHOR"]
    """
    The type of event anchor this is, can be: "CONTACT_PROPERTY_ANCHOR" or
    "STATIC_DATE_ANCHOR"
    """

    year: Optional[int] = None
    """The year of the date to anchor on.

    If this is not provided then this flow will re-run each year.
    """
