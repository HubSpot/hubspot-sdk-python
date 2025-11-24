# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["NumberPropertyOperation"]


class NumberPropertyOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    operation_type: str = FieldInfo(alias="operationType")

    operator: Literal[
        "HAS_EVER_BEEN_EQUAL_TO",
        "HAS_NEVER_BEEN_EQUAL_TO",
        "IS_EQUAL_TO",
        "IS_GREATER_THAN",
        "IS_GREATER_THAN_OR_EQUAL_TO",
        "IS_LESS_THAN",
        "IS_LESS_THAN_OR_EQUAL_TO",
        "IS_NOT_EQUAL_TO",
    ]

    operator_name: str = FieldInfo(alias="operatorName")

    property_type: Literal["number"] = FieldInfo(alias="propertyType")

    value: float

    default_value: Optional[str] = FieldInfo(alias="defaultValue", default=None)
