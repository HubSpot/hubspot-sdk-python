# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .email_statistic_interval import EmailStatisticInterval

__all__ = ["CollectionResponseWithTotalEmailStatisticIntervalNoPaging"]


class CollectionResponseWithTotalEmailStatisticIntervalNoPaging(BaseModel):
    results: List[EmailStatisticInterval]
    """Collection of objects."""

    total: int
    """Total number of objects."""
