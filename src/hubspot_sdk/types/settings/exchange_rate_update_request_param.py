# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ExchangeRateUpdateRequestParam"]


class ExchangeRateUpdateRequestParam(TypedDict, total=False):
    id: Required[str]

    conversion_rate: Required[Annotated[float, PropertyInfo(alias="conversionRate")]]

    effective_at: Annotated[Union[str, datetime], PropertyInfo(alias="effectiveAt", format="iso8601")]
