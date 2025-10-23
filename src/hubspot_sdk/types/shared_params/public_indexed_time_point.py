# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .public_index_offset import PublicIndexOffset
from .public_now_reference import PublicNowReference
from .public_week_reference import PublicWeekReference
from .public_year_reference import PublicYearReference
from .public_month_reference import PublicMonthReference
from .public_today_reference import PublicTodayReference
from .public_quarter_reference import PublicQuarterReference
from .public_fiscal_year_reference import PublicFiscalYearReference
from .public_fiscal_quarter_reference import PublicFiscalQuarterReference

__all__ = ["PublicIndexedTimePoint", "IndexReference"]

IndexReference: TypeAlias = Union[
    PublicNowReference,
    PublicTodayReference,
    PublicWeekReference,
    PublicFiscalQuarterReference,
    PublicFiscalYearReference,
    PublicYearReference,
    PublicQuarterReference,
    PublicMonthReference,
]


class PublicIndexedTimePoint(TypedDict, total=False):
    index_reference: Required[Annotated[IndexReference, PropertyInfo(alias="indexReference")]]

    time_type: Required[Annotated[Literal["INDEXED"], PropertyInfo(alias="timeType")]]

    zone_id: Required[Annotated[str, PropertyInfo(alias="zoneId")]]

    offset: PublicIndexOffset

    timezone_source: Annotated[str, PropertyInfo(alias="timezoneSource")]
