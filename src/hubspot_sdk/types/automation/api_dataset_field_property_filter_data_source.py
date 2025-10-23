# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .api_sort import APISort
from ..._models import BaseModel

__all__ = ["APIDatasetFieldPropertyFilterDataSource"]


class APIDatasetFieldPropertyFilterDataSource(BaseModel):
    dataset_field_name: str = FieldInfo(alias="datasetFieldName")

    name: str

    property_name: str = FieldInfo(alias="propertyName")

    type: Literal["DATASET_FIELD_PROPERTY_FILTER"]

    sort_by: Optional[APISort] = FieldInfo(alias="sortBy", default=None)
