# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ExchangeRateUpdateExchangeRateParams"]


class ExchangeRateUpdateExchangeRateParams(TypedDict, total=False):
    conversion_rate: Required[Annotated[float, PropertyInfo(alias="conversionRate")]]
    """
    The updated conversion rate between the to and from currency code of this
    exchange rate.
    """

    effective_at: Annotated[Union[str, datetime], PropertyInfo(alias="effectiveAt", format="iso8601")]
    """The date the exchange rate is in effect."""
