# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel
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

IndexReference: TypeAlias = Annotated[
    Union[
        PublicNowReference,
        PublicTodayReference,
        PublicWeekReference,
        PublicFiscalQuarterReference,
        PublicFiscalYearReference,
        PublicYearReference,
        PublicQuarterReference,
        PublicMonthReference,
    ],
    PropertyInfo(discriminator="reference_type"),
]


class PublicIndexedTimePoint(BaseModel):
    index_reference: IndexReference = FieldInfo(alias="indexReference")
    """Specifies the reference point in time for the indexed time point."""

    time_type: Literal["INDEXED"] = FieldInfo(alias="timeType")
    """Defines the type of time (INDEXED)."""

    zone_id: str = FieldInfo(alias="zoneId")
    """
    Indicates the identifier for the time zone associated with the indexed time
    point.
    """

    offset: Optional[PublicIndexOffset] = None

    timezone_source: Optional[str] = FieldInfo(alias="timezoneSource", default=None)
    """
    Specifies the source of the time zone information for the indexed time point
    (CUSTOM, USER, PORTAL).
    """
