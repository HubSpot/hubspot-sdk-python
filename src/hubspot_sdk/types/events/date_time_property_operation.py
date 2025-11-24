# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DateTimePropertyOperation"]


class DateTimePropertyOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    operation_type: str = FieldInfo(alias="operationType")

    operator: Literal["IS_AFTER", "IS_AFTER_DATE", "IS_BEFORE", "IS_BEFORE_DATE", "IS_EQUAL_TO"]

    operator_name: str = FieldInfo(alias="operatorName")

    property_type: Literal["datetime"] = FieldInfo(alias="propertyType")

    requires_time_zone_conversion: bool = FieldInfo(alias="requiresTimeZoneConversion")

    timestamp: int

    default_value: Optional[str] = FieldInfo(alias="defaultValue", default=None)
