# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .email_statistics_data import EmailStatisticsData

__all__ = ["AggregateEmailStatistics"]


class AggregateEmailStatistics(BaseModel):
    aggregate: Optional[EmailStatisticsData] = None

    campaign_aggregations: Optional[Dict[str, EmailStatisticsData]] = FieldInfo(
        alias="campaignAggregations", default=None
    )
    """The aggregated statistics per campaign."""

    emails: Optional[List[int]] = None
    """List of email IDs that were sent during the time span."""
