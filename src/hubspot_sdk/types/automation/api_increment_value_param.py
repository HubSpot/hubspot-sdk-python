# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIIncrementValueParam"]


class APIIncrementValueParam(TypedDict, total=False):
    increment_amount: Required[Annotated[float, PropertyInfo(alias="incrementAmount")]]

    type: Required[Literal["INCREMENT"]]
