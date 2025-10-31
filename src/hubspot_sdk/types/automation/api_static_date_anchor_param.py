# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIStaticDateAnchorParam"]


class APIStaticDateAnchorParam(TypedDict, total=False):
    day_of_month: Required[Annotated[int, PropertyInfo(alias="dayOfMonth")]]

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

    type: Required[Literal["STATIC_DATE_ANCHOR"]]

    year: int
