# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIStaticDateAnchorParam"]


class APIStaticDateAnchorParam(TypedDict, total=False):
    day_of_month: Required[Annotated[int, PropertyInfo(alias="dayOfMonth")]]
    """The day of the date to anchor on"""

    month: Required[
        Literal[
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
    ]
    """The month of the date to anchor on"""

    type: Required[Literal["STATIC_DATE_ANCHOR"]]
    """
    The type of event anchor this is, can be: "CONTACT_PROPERTY_ANCHOR" or
    "STATIC_DATE_ANCHOR"
    """

    year: int
    """The year of the date to anchor on.

    If this is not provided then this flow will re-run each year.
    """
