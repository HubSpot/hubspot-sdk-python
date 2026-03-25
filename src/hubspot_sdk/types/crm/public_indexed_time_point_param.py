# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .public_index_offset_param import PublicIndexOffsetParam
from .public_now_reference_param import PublicNowReferenceParam
from .public_week_reference_param import PublicWeekReferenceParam
from .public_year_reference_param import PublicYearReferenceParam
from .public_month_reference_param import PublicMonthReferenceParam
from .public_today_reference_param import PublicTodayReferenceParam
from .public_quarter_reference_param import PublicQuarterReferenceParam
from .public_fiscal_year_reference_param import PublicFiscalYearReferenceParam
from .public_fiscal_quarter_reference_param import PublicFiscalQuarterReferenceParam

__all__ = ["PublicIndexedTimePointParam", "IndexReference"]

IndexReference: TypeAlias = Union[
    PublicNowReferenceParam,
    PublicTodayReferenceParam,
    PublicWeekReferenceParam,
    PublicFiscalQuarterReferenceParam,
    PublicFiscalYearReferenceParam,
    PublicYearReferenceParam,
    PublicQuarterReferenceParam,
    PublicMonthReferenceParam,
]


class PublicIndexedTimePointParam(TypedDict, total=False):
    index_reference: Required[Annotated[IndexReference, PropertyInfo(alias="indexReference")]]
    """Specifies the reference point in time for the indexed time point."""

    time_type: Required[Annotated[Literal["INDEXED"], PropertyInfo(alias="timeType")]]
    """Defines the type of time (INDEXED)."""

    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]
    """
    Indicates the identifier for the time zone associated with the indexed time
    point.
    """

    offset: PublicIndexOffsetParam

    timezone_source: Annotated[str, PropertyInfo(alias="timezoneSource")]
    """
    Specifies the source of the time zone information for the indexed time point
    (CUSTOM, USER, PORTAL).
    """
