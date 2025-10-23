# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .api_sort_param import APISortParam

__all__ = ["APIDatasetFieldPropertyFilterDataSourceParam"]


class APIDatasetFieldPropertyFilterDataSourceParam(TypedDict, total=False):
    dataset_field_name: Required[Annotated[str, PropertyInfo(alias="datasetFieldName")]]

    name: Required[str]

    property_name: Required[Annotated[str, PropertyInfo(alias="propertyName")]]

    type: Required[Literal["DATASET_FIELD_PROPERTY_FILTER"]]

    sort_by: Annotated[APISortParam, PropertyInfo(alias="sortBy")]
