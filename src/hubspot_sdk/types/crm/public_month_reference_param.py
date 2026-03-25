# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicMonthReferenceParam"]


class PublicMonthReferenceParam(TypedDict, total=False):
    day: Required[int]
    """The day component of the month reference."""

    reference_type: Required[Annotated[Literal["MONTH"], PropertyInfo(alias="referenceType")]]
    """Indicates the type of reference, (MONTH)."""

    hour: int
    """The hour component of the month reference."""

    millisecond: int
    """The millisecond component of the month reference."""

    minute: int
    """The minute component of the month reference."""

    second: int
    """The second component of the month reference."""
