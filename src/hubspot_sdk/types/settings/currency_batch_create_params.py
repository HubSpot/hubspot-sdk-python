# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .exchange_rate_create_request_param import ExchangeRateCreateRequestParam

__all__ = ["CurrencyBatchCreateParams"]


class CurrencyBatchCreateParams(TypedDict, total=False):
    inputs: Required[Iterable[ExchangeRateCreateRequestParam]]
