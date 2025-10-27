# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AssetListParams"]


class AssetListParams(TypedDict, total=False):
    campaign_guid: Required[Annotated[str, PropertyInfo(alias="campaignGuid")]]

    after: str
    """A cursor for pagination.

    If provided, the results will start after the given cursor. Example:
    NTI1Cg%3D%3D
    """

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """End date to fetch asset metrics, formatted as YYYY-MM-DD.

    This date is used to fetch the metrics associated with the assets for a
    specified period. If not provided, no asset metrics will be fetched.
    """

    limit: str
    """The maximum number of results to return. Default: 10"""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Start date to fetch asset metrics, formatted as YYYY-MM-DD.

    This date is used to fetch the metrics associated with the assets for a
    specified period. If not provided, no asset metrics will be fetched.
    """
