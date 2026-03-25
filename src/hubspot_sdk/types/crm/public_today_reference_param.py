# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicTodayReferenceParam"]


class PublicTodayReferenceParam(TypedDict, total=False):
    reference_type: Required[Annotated[Literal["TODAY"], PropertyInfo(alias="referenceType")]]
    """Indicates the type of reference (TODAY)."""

    hour: int
    """The hour component of the current day reference."""

    millisecond: int
    """The millisecond component of the current day reference."""

    minute: int
    """The minute component of the current day reference."""

    second: int
    """The second component of the current day reference."""
