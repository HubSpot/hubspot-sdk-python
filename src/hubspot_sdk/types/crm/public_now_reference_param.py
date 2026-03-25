# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicNowReferenceParam"]


class PublicNowReferenceParam(TypedDict, total=False):
    reference_type: Required[Annotated[Literal["NOW"], PropertyInfo(alias="referenceType")]]
    """Indicates the type of reference (NOW)."""

    hour: int
    """The hour component of the current time reference."""

    millisecond: int
    """The millisecond component of the current time reference."""

    minute: int
    """The minute component of the current time reference."""

    second: int
    """The second component of the current time reference."""
