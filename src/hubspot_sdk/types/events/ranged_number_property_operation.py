# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RangedNumberPropertyOperation"]


class RangedNumberPropertyOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    lower_bound: int = FieldInfo(alias="lowerBound")

    operation_type: str = FieldInfo(alias="operationType")

    operator: Literal["IS_BETWEEN", "IS_NOT_BETWEEN"]

    operator_name: str = FieldInfo(alias="operatorName")

    property_type: Literal["number-ranged"] = FieldInfo(alias="propertyType")

    upper_bound: int = FieldInfo(alias="upperBound")

    default_value: Optional[str] = FieldInfo(alias="defaultValue", default=None)
