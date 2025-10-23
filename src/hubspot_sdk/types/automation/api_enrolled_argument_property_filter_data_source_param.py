# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .api_sort_param import APISortParam

__all__ = ["APIEnrolledArgumentPropertyFilterDataSourceParam"]


class APIEnrolledArgumentPropertyFilterDataSourceParam(TypedDict, total=False):
    argument_name: Required[Annotated[str, PropertyInfo(alias="argumentName")]]

    name: Required[str]

    property_name: Required[Annotated[str, PropertyInfo(alias="propertyName")]]

    type: Required[Literal["ENROLLED_ARGUMENT_PROPERTY_FILTER"]]

    sort_by: Annotated[APISortParam, PropertyInfo(alias="sortBy")]
