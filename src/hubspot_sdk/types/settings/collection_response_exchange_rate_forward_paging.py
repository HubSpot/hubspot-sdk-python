# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .exchange_rate import ExchangeRate
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponseExchangeRateForwardPaging"]


class CollectionResponseExchangeRateForwardPaging(BaseModel):
    results: List[ExchangeRate]

    paging: Optional[ForwardPaging] = None
