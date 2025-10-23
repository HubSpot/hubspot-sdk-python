# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicRangedDatePropertyOperation"]


class PublicRangedDatePropertyOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    lower_bound: int = FieldInfo(alias="lowerBound")

    operation_type: Literal["RANGED_DATE"] = FieldInfo(alias="operationType")

    operator: str

    requires_time_zone_conversion: bool = FieldInfo(alias="requiresTimeZoneConversion")

    upper_bound: int = FieldInfo(alias="upperBound")
