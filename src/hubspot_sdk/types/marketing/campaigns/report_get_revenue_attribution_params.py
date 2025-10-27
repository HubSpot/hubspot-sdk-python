# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ReportGetRevenueAttributionParams"]


class ReportGetRevenueAttributionParams(TypedDict, total=False):
    attribution_model: Annotated[str, PropertyInfo(alias="attributionModel")]
    """
    Allowed values: LINEAR, FIRST_INTERACTION, LAST_INTERACTION, FULL_PATH,
    U_SHAPED, W_SHAPED, TIME_DECAY, J_SHAPED, INVERSE_J_SHAPED Default value: LINEAR
    """

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
