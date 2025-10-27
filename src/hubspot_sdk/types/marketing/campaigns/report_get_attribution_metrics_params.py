# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ReportGetAttributionMetricsParams"]


class ReportGetAttributionMetricsParams(TypedDict, total=False):
    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """
    End date for the report data, formatted as YYYY-MM-DD. Default value: Current
    date
    """

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """
    The start date for the report data, formatted as YYYY-MM-DD. Default value:
    2006-01-01
    """
