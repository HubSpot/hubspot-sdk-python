# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ComparativeBoolPropertyOperation"]


class ComparativeBoolPropertyOperation(BaseModel):
    comparison_property_name: str = FieldInfo(alias="comparisonPropertyName")

    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    operation_type: str = FieldInfo(alias="operationType")

    operator: Literal["IS_EQUAL_TO", "IS_NOT_EQUAL_TO"]

    operator_name: str = FieldInfo(alias="operatorName")

    property_type: Literal["bool-comparative"] = FieldInfo(alias="propertyType")

    default_value: Optional[str] = FieldInfo(alias="defaultValue", default=None)

    render_spec: Optional[str] = FieldInfo(alias="renderSpec", default=None)
