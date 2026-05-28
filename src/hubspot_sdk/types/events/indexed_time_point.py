# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .fiscal_year import FiscalYear
from .index_offset import IndexOffset
from .now_reference import NowReference
from .fiscal_quarter import FiscalQuarter
from .week_reference import WeekReference
from .year_reference import YearReference
from .month_reference import MonthReference
from .today_reference import TodayReference
from .quarter_reference import QuarterReference

__all__ = ["IndexedTimePoint", "IndexReference"]

IndexReference: TypeAlias = Annotated[
    Union[
        NowReference,
        TodayReference,
        WeekReference,
        MonthReference,
        QuarterReference,
        FiscalQuarter,
        YearReference,
        FiscalYear,
    ],
    PropertyInfo(discriminator="reference_type"),
]


class IndexedTimePoint(BaseModel):
    index_reference: IndexReference = FieldInfo(alias="indexReference")

    time_type: Literal["INDEXED"] = FieldInfo(alias="timeType")

    timezone_source: Literal["CUSTOM", "PORTAL", "USER"] = FieldInfo(alias="timezoneSource")

    zone_id: str = FieldInfo(alias="zoneId")

    offset: Optional[IndexOffset] = None

    should_generate_refresh_time: Optional[bool] = FieldInfo(alias="shouldGenerateRefreshTime", default=None)
