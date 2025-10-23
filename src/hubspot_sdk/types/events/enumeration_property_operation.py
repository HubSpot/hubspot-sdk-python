# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EnumerationPropertyOperation"]


class EnumerationPropertyOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    operation_type: str = FieldInfo(alias="operationType")

    operator: Literal[
        "IS_ANY_OF",
        "IS_NONE_OF",
        "IS_EXACTLY",
        "IS_NOT_EXACTLY",
        "CONTAINS_ALL",
        "DOES_NOT_CONTAIN_ALL",
        "HAS_EVER_BEEN_ANY_OF",
        "HAS_NEVER_BEEN_ANY_OF",
        "HAS_EVER_BEEN_EXACTLY",
        "HAS_NEVER_BEEN_EXACTLY",
        "HAS_EVER_CONTAINED_ALL",
        "HAS_NEVER_CONTAINED_ALL",
    ]

    operator_name: str = FieldInfo(alias="operatorName")

    property_type: Literal["enumeration"] = FieldInfo(alias="propertyType")

    values: List[str]

    default_value: Optional[str] = FieldInfo(alias="defaultValue", default=None)
