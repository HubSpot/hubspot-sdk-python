# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["MetricGetRevenueAttributionParams"]


class MetricGetRevenueAttributionParams(TypedDict, total=False):
    attribution_model: Annotated[str, PropertyInfo(alias="attributionModel")]
    """The model used to attribute revenue to the campaign."""

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """End date to fetch attribution data, YYYY-MM-DD."""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Start date to fetch attribution data, YYYY-MM-DD."""
