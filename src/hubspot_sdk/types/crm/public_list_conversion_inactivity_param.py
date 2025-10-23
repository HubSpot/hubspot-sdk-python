# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicListConversionInactivityParam"]


class PublicListConversionInactivityParam(TypedDict, total=False):
    conversion_type: Required[Annotated[Literal["INACTIVITY"], PropertyInfo(alias="conversionType")]]

    offset: Required[int]

    time_unit: Required[Annotated[Literal["DAY", "WEEK", "MONTH"], PropertyInfo(alias="timeUnit")]]
