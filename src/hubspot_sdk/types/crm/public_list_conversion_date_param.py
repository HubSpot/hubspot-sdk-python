# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicListConversionDateParam"]


class PublicListConversionDateParam(TypedDict, total=False):
    conversion_type: Required[Annotated[Literal["CONVERSION_DATE"], PropertyInfo(alias="conversionType")]]
    """Specifies the type of conversion (CONVERSION_DATE)."""

    day: Required[int]
    """The day component of the conversion date."""

    month: Required[int]
    """The month component of the conversion date."""

    year: Required[int]
    """The year component of the conversion date."""
