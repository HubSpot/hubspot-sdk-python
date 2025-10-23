# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .api_sort_param import APISortParam

__all__ = ["APIStaticPropertyFilterDataSourceParam"]


class APIStaticPropertyFilterDataSourceParam(TypedDict, total=False):
    name: Required[str]

    property_name: Required[Annotated[str, PropertyInfo(alias="propertyName")]]

    static_value: Required[Annotated[str, PropertyInfo(alias="staticValue")]]

    type: Required[Literal["STATIC_PROPERTY_FILTER"]]

    sort_by: Annotated[APISortParam, PropertyInfo(alias="sortBy")]
