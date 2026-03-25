# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicRangedDatePropertyOperation"]


class PublicRangedDatePropertyOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")
    """
    Specifies whether objects without a set value should be included in the
    operation.
    """

    lower_bound: int = FieldInfo(alias="lowerBound")
    """The lower limit of the date range for the operation."""

    operation_type: Literal["RANGED_DATE"] = FieldInfo(alias="operationType")
    """Specifies the type of operation (RANGED_DATE)."""

    operator: str
    """
    Defines the operation to be applied in the ranged date property operation
    (IS_BETWEEN, IS_NOT_BETWEEN).
    """

    requires_time_zone_conversion: bool = FieldInfo(alias="requiresTimeZoneConversion")
    """Indicates whether the operation requires conversion to a different time zone."""

    upper_bound: int = FieldInfo(alias="upperBound")
    """The upper limit of the date range for the operation."""
