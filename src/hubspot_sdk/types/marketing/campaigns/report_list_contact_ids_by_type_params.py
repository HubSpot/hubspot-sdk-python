# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ReportListContactIDsByTypeParams"]


class ReportListContactIDsByTypeParams(TypedDict, total=False):
    campaign_guid: Required[Annotated[str, PropertyInfo(alias="campaignGuid")]]

    after: str
    """A cursor for pagination.

    If provided, the results will start after the given cursor. Example:
    NTI1Cg%3D%3D
    """

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """
    End date for the report data, formatted as YYYY-MM-DD. Default value: Current
    date
    """

    limit: int
    """Limit for the number of contacts to fetch Default: 100"""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """
    The start date for the report data, formatted as YYYY-MM-DD. Default value:
    2006-01-01
    """
