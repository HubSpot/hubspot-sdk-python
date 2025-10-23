# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicRollingDateRangePropertyOperation"]


class PublicRollingDateRangePropertyOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    number_of_days: int = FieldInfo(alias="numberOfDays")

    operation_type: Literal["ROLLING_DATE_RANGE"] = FieldInfo(alias="operationType")

    operator: str

    requires_time_zone_conversion: bool = FieldInfo(alias="requiresTimeZoneConversion")
