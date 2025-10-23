# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RollingDateRangePropertyOperation"]


class RollingDateRangePropertyOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    number_of_days: int = FieldInfo(alias="numberOfDays")

    operation_type: str = FieldInfo(alias="operationType")

    operator: Literal[
        "IS_LESS_THAN_X_DAYS_AGO",
        "IS_MORE_THAN_X_DAYS_AGO",
        "IS_LESS_THAN_X_DAYS_FROM_NOW",
        "IS_MORE_THAN_X_DAYS_FROM_NOW",
    ]

    operator_name: str = FieldInfo(alias="operatorName")

    property_type: Literal["datetime-rolling"] = FieldInfo(alias="propertyType")

    requires_time_zone_conversion: bool = FieldInfo(alias="requiresTimeZoneConversion")

    default_value: Optional[str] = FieldInfo(alias="defaultValue", default=None)
