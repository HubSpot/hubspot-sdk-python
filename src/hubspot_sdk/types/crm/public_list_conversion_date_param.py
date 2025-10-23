# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicListConversionDateParam"]


class PublicListConversionDateParam(TypedDict, total=False):
    conversion_type: Required[Annotated[Literal["CONVERSION_DATE"], PropertyInfo(alias="conversionType")]]

    day: Required[int]

    month: Required[int]

    year: Required[int]
