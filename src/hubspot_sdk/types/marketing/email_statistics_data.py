# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EmailStatisticsData"]


class EmailStatisticsData(BaseModel):
    counters: Dict[str, int]
    """Counters like number of `sent`, `open` or `delivered`."""

    device_breakdown: Dict[str, Dict[str, int]] = FieldInfo(alias="deviceBreakdown")
    """Statistics by device."""

    qualifier_stats: Dict[str, Dict[str, int]] = FieldInfo(alias="qualifierStats")
    """Number of emails that were dropped and bounced."""

    ratios: Dict[str, float]
    """Ratios like `openratio` or `clickratio`"""
