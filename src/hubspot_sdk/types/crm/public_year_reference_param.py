# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicYearReferenceParam"]


class PublicYearReferenceParam(TypedDict, total=False):
    day: Required[int]
    """The day component of the year reference."""

    month: Required[int]
    """The month component of the year reference."""

    reference_type: Required[Annotated[Literal["YEAR"], PropertyInfo(alias="referenceType")]]
    """Indicates the type of reference (YEAR)."""

    hour: int
    """The hour component of the year reference."""

    millisecond: int
    """The millisecond component of the year reference."""

    minute: int
    """The minute component of the year reference."""

    second: int
    """The second component of the year reference."""
