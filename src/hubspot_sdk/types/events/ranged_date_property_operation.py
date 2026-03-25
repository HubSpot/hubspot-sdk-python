# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RangedDatePropertyOperation"]


class RangedDatePropertyOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    lower_bound_timestamp: int = FieldInfo(alias="lowerBoundTimestamp")

    operation_type: str = FieldInfo(alias="operationType")

    operator: Literal["IS_BETWEEN", "IS_NOT_BETWEEN"]

    operator_name: str = FieldInfo(alias="operatorName")

    property_type: Literal["datetime-ranged"] = FieldInfo(alias="propertyType")

    requires_time_zone_conversion: bool = FieldInfo(alias="requiresTimeZoneConversion")

    upper_bound_timestamp: int = FieldInfo(alias="upperBoundTimestamp")

    default_value: Optional[str] = FieldInfo(alias="defaultValue", default=None)

    render_spec: Optional[str] = FieldInfo(alias="renderSpec", default=None)
