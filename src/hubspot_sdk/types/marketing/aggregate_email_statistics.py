# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .email_statistics_data import EmailStatisticsData

__all__ = ["AggregateEmailStatistics"]


class AggregateEmailStatistics(BaseModel):
    aggregate: EmailStatisticsData

    campaign_aggregations: Dict[str, EmailStatisticsData] = FieldInfo(alias="campaignAggregations")
    """The aggregated statistics per campaign."""

    emails: List[int]
    """List of email IDs that were sent during the time span."""
