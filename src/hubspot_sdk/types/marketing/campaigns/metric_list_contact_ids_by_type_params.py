# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["MetricListContactIDsByTypeParams"]


class MetricListContactIDsByTypeParams(TypedDict, total=False):
    campaign_guid: Required[Annotated[str, PropertyInfo(alias="campaignGuid")]]

    after: str
    """
    The paging cursor token of the last successfully read resource, used for
    pagination.
    """

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """The end date for filtering contacts, formatted as a string."""

    limit: int
    """The maximum number of results to display per page."""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """The start date for filtering contacts, formatted as a string."""
