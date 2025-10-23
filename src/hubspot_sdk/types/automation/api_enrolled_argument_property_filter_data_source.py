# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .api_sort import APISort
from ..._models import BaseModel

__all__ = ["APIEnrolledArgumentPropertyFilterDataSource"]


class APIEnrolledArgumentPropertyFilterDataSource(BaseModel):
    argument_name: str = FieldInfo(alias="argumentName")

    name: str

    property_name: str = FieldInfo(alias="propertyName")

    type: Literal["ENROLLED_ARGUMENT_PROPERTY_FILTER"]

    sort_by: Optional[APISort] = FieldInfo(alias="sortBy", default=None)
