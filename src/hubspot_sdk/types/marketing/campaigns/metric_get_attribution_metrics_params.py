# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["MetricGetAttributionMetricsParams"]


class MetricGetAttributionMetricsParams(TypedDict, total=False):
    end_date: Annotated[str, PropertyInfo(alias="endDate")]

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
