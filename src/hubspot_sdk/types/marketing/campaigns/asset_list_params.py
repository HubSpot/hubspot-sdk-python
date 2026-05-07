# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AssetListParams"]


class AssetListParams(TypedDict, total=False):
    campaign_guid: Required[Annotated[str, PropertyInfo(alias="campaignGuid")]]

    after: str
    """
    The paging cursor token of the last successfully read resource will be returned
    as the `paging.next.after` JSON property of a paged response containing more
    results.
    """

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """End date to fetch asset metrics, formatted as YYYY-MM-DD.

    This date is used to fetch the metrics associated with the assets for a
    specified period. If not provided, no asset metrics will be fetched. Example:
    2024-01-27
    """

    limit: str
    """The maximum number of results to display per page."""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Start date to fetch asset metrics, formatted as YYYY-MM-DD.

    This date is used to fetch the metrics associated with the assets for a
    specified period. If not provided, no asset metrics will be fetched. Example:
    2023-01-20
    """
