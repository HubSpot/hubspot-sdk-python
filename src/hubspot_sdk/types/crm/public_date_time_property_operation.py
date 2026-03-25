# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicDateTimePropertyOperation"]


class PublicDateTimePropertyOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")
    """
    Specifies whether objects without a set value should be included in the
    operation.
    """

    operation_type: Literal["DATETIME"] = FieldInfo(alias="operationType")
    """The type of operation (DATETIME)."""

    operator: str
    """
    Defines the operation to be applied, such as comparison operators (IS_BEFORE,
    IS_AFTER).
    """

    requires_time_zone_conversion: bool = FieldInfo(alias="requiresTimeZoneConversion")
    """Indicates whether the timestamp requires conversion to a different time zone."""

    timestamp: int
    """The specific point in time used in the operation."""
