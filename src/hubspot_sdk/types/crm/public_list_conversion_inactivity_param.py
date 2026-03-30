# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicListConversionInactivityParam"]


class PublicListConversionInactivityParam(TypedDict, total=False):
    conversion_type: Required[Annotated[Literal["INACTIVITY"], PropertyInfo(alias="conversionType")]]
    """Specifies the type of conversion (INACTIVITY)."""

    offset: Required[int]
    """Value used to paginate through lists.

    The `offset` provided in the response can be used in the next request to fetch
    the next page of results. Defaults to `0` if no offset is provided.
    """

    time_unit: Required[Annotated[Literal["DAY", "MONTH", "WEEK"], PropertyInfo(alias="timeUnit")]]
    """The unit of time for the inactivity period, such as (DAY, MONTH, WEEK)."""
