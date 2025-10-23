# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ListScheduleConversionParams", "PublicListConversionDate", "PublicListConversionInactivity"]


class PublicListConversionDate(TypedDict, total=False):
    conversion_type: Required[Annotated[Literal["CONVERSION_DATE"], PropertyInfo(alias="conversionType")]]

    day: Required[int]

    month: Required[int]

    year: Required[int]


class PublicListConversionInactivity(TypedDict, total=False):
    conversion_type: Required[Annotated[Literal["INACTIVITY"], PropertyInfo(alias="conversionType")]]

    offset: Required[int]

    time_unit: Required[Annotated[Literal["DAY", "WEEK", "MONTH"], PropertyInfo(alias="timeUnit")]]


ListScheduleConversionParams: TypeAlias = Union[PublicListConversionDate, PublicListConversionInactivity]
