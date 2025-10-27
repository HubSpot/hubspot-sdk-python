# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CentralExchangeRatesInformation"]


class CentralExchangeRatesInformation(BaseModel):
    central_exchange_rates_enabled: bool = FieldInfo(alias="centralExchangeRatesEnabled")
