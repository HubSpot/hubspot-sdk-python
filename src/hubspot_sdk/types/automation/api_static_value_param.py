# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIStaticValueParam"]


class APIStaticValueParam(TypedDict, total=False):
    static_value: Required[Annotated[str, PropertyInfo(alias="staticValue")]]

    type: Required[Literal["STATIC_VALUE"]]
