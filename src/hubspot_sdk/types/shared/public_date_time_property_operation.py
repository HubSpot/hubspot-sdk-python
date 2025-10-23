# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicDateTimePropertyOperation"]


class PublicDateTimePropertyOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    operation_type: Literal["DATETIME"] = FieldInfo(alias="operationType")

    operator: str

    requires_time_zone_conversion: bool = FieldInfo(alias="requiresTimeZoneConversion")

    timestamp: int
