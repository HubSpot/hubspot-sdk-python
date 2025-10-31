# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIAppendObjectPropertyValueParam"]


class APIAppendObjectPropertyValueParam(TypedDict, total=False):
    append_property_name: Required[Annotated[str, PropertyInfo(alias="appendPropertyName")]]

    type: Required[Literal["APPEND_OBJECT_PROPERTY"]]
