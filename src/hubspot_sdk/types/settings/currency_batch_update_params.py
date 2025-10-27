# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .exchange_rate_update_request_param import ExchangeRateUpdateRequestParam

__all__ = ["CurrencyBatchUpdateParams"]


class CurrencyBatchUpdateParams(TypedDict, total=False):
    inputs: Required[Iterable[ExchangeRateUpdateRequestParam]]
