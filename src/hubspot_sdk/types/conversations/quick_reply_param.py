# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["QuickReplyParam"]


class QuickReplyParam(TypedDict, total=False):
    value: Required[str]

    value_type: Required[Annotated[str, PropertyInfo(alias="valueType")]]

    label: str
