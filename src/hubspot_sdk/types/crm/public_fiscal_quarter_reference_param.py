# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicFiscalQuarterReferenceParam"]


class PublicFiscalQuarterReferenceParam(TypedDict, total=False):
    day: Required[int]
    """The day component of the fiscal quarter reference."""

    month: Required[int]
    """The month component of the fiscal quarter reference."""

    reference_type: Required[Annotated[Literal["FISCAL_QUARTER"], PropertyInfo(alias="referenceType")]]
    """Indicates the type of reference (FISCAL_QUARTER)."""

    hour: int
    """The hour component of the fiscal quarter reference."""

    millisecond: int
    """The millisecond component of the fiscal quarter reference."""

    minute: int
    """The minute component of the fiscal quarter reference."""

    second: int
    """The second component of the fiscal quarter reference."""
