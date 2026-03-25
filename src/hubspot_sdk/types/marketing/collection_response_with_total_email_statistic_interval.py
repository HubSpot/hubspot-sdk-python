# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from .email_statistic_interval import EmailStatisticInterval

__all__ = ["CollectionResponseWithTotalEmailStatisticInterval"]


class CollectionResponseWithTotalEmailStatisticInterval(BaseModel):
    results: List[EmailStatisticInterval]

    total: int

    paging: Optional[Paging] = None
