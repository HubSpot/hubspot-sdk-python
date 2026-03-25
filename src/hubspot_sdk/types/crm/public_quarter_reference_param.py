# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicQuarterReferenceParam"]


class PublicQuarterReferenceParam(TypedDict, total=False):
    day: Required[int]
    """The day component of the quarter reference."""

    month: Required[int]
    """The month component of the quarter reference."""

    reference_type: Required[Annotated[Literal["QUARTER"], PropertyInfo(alias="referenceType")]]
    """Indicates the type of reference (QUARTER)."""

    hour: int
    """The hour component of the quarter reference."""

    millisecond: int
    """The millisecond component of the quarter reference."""

    minute: int
    """The minute component of the quarter reference."""

    second: int
    """The second component of the quarter reference."""
