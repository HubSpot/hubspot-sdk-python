# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicTimeOffset"]


class PublicTimeOffset(TypedDict, total=False):
    amount: Required[int]

    offset_direction: Required[Annotated[str, PropertyInfo(alias="offsetDirection")]]

    time_unit: Required[Annotated[str, PropertyInfo(alias="timeUnit")]]
