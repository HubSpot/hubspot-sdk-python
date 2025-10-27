# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .currency_code_info import CurrencyCodeInfo

__all__ = ["CollectionResponseCurrencyCodeInfoNoPaging"]


class CollectionResponseCurrencyCodeInfoNoPaging(BaseModel):
    results: List[CurrencyCodeInfo]
