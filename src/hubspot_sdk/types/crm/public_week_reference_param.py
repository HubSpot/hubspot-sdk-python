# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicWeekReferenceParam"]


class PublicWeekReferenceParam(TypedDict, total=False):
    day_of_week: Required[
        Annotated[
            Literal["FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"],
            PropertyInfo(alias="dayOfWeek"),
        ]
    ]
    """
    The day of the week (SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY,
    SATURDAY).
    """

    reference_type: Required[Annotated[Literal["WEEK"], PropertyInfo(alias="referenceType")]]
    """Indicates the type of reference (WEEK)."""

    hour: int
    """The hour component of the week reference."""

    millisecond: int
    """The millisecond component of the week reference."""

    minute: int
    """The minute component of the week reference."""

    second: int
    """The second component of the week reference."""
