# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .exchange_rate import ExchangeRate

__all__ = ["CollectionResponseExchangeRateNoPaging"]


class CollectionResponseExchangeRateNoPaging(BaseModel):
    results: List[ExchangeRate]
