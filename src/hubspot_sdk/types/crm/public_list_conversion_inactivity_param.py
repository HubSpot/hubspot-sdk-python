# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicListConversionInactivityParam"]


class PublicListConversionInactivityParam(TypedDict, total=False):
    conversion_type: Required[Annotated[Literal["INACTIVITY"], PropertyInfo(alias="conversionType")]]
    """Specifies the type of conversion (INACTIVITY)."""

    offset: Required[int]
    """The number of time units for the inactivity period."""

    time_unit: Required[Annotated[Literal["DAY", "MONTH", "WEEK"], PropertyInfo(alias="timeUnit")]]
    """The unit of time for the inactivity period, such as (DAY, MONTH, WEEK)."""
