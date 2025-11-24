# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicWeekReference"]


class PublicWeekReference(TypedDict, total=False):
    day_of_week: Required[
        Annotated[
            Literal["FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"],
            PropertyInfo(alias="dayOfWeek"),
        ]
    ]

    reference_type: Required[Annotated[Literal["WEEK"], PropertyInfo(alias="referenceType")]]

    hour: int

    millisecond: int

    minute: int

    second: int
