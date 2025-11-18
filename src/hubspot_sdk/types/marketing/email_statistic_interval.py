# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .interval import Interval
from ..._models import BaseModel
from .email_statistics_data import EmailStatisticsData

__all__ = ["EmailStatisticInterval"]


class EmailStatisticInterval(BaseModel):
    aggregations: EmailStatisticsData

    interval: Interval
