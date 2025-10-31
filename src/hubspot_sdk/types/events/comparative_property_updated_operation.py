# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ComparativePropertyUpdatedOperation"]


class ComparativePropertyUpdatedOperation(BaseModel):
    comparison_property_name: str = FieldInfo(alias="comparisonPropertyName")

    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    operation_type: str = FieldInfo(alias="operationType")

    operator: Literal["IS_BEFORE", "IS_AFTER"]

    operator_name: str = FieldInfo(alias="operatorName")

    property_type: Literal["property-updated-comparative"] = FieldInfo(alias="propertyType")

    default_comparison_value: Optional[str] = FieldInfo(alias="defaultComparisonValue", default=None)

    default_value: Optional[str] = FieldInfo(alias="defaultValue", default=None)
