# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicComparativePropertyUpdatedOperation"]


class PublicComparativePropertyUpdatedOperation(BaseModel):
    comparison_property_name: str = FieldInfo(alias="comparisonPropertyName")

    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    operation_type: Literal["COMPARATIVE_PROPERTY_UPDATED"] = FieldInfo(alias="operationType")

    operator: str

    default_comparison_value: Optional[str] = FieldInfo(alias="defaultComparisonValue", default=None)
