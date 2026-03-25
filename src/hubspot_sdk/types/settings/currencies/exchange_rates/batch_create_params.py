# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ...exchange_rate_create_request_param import ExchangeRateCreateRequestParam

__all__ = ["BatchCreateParams"]


class BatchCreateParams(TypedDict, total=False):
    inputs: Required[Iterable[ExchangeRateCreateRequestParam]]
