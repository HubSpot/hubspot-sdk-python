# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CurrencyCodeInfo"]


class CurrencyCodeInfo(BaseModel):
    currency_code: str = FieldInfo(alias="currencyCode")

    currency_name: str = FieldInfo(alias="currencyName")
