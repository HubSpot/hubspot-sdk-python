# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["APIObjectPropertyValueParam"]


class APIObjectPropertyValueParam(TypedDict, total=False):
    property_name: Required[Annotated[str, PropertyInfo(alias="propertyName")]]

    type: Required[Literal["OBJECT_PROPERTY"]]
