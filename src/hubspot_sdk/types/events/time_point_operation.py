# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .date_point import DatePoint
from .indexed_time_point import IndexedTimePoint
from .property_referenced_time import PropertyReferencedTime

__all__ = ["TimePointOperation", "TimePoint"]

TimePoint: TypeAlias = Union[DatePoint, IndexedTimePoint, PropertyReferencedTime]


class TimePointOperation(BaseModel):
    endpoint_behavior: Literal["INCLUSIVE", "EXCLUSIVE"] = FieldInfo(alias="endpointBehavior")

    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    operation_type: str = FieldInfo(alias="operationType")

    operator: Literal["IS_BEFORE", "IS_AFTER"]

    operator_name: str = FieldInfo(alias="operatorName")

    property_parser: Literal[
        "VALUE",
        "UPDATED_AT",
        "ANNIVERSARY",
        "VALUE_WITH_ZONE_SAME_LOCAL_CONVERSION",
        "ANNIVERSARY_WITH_ZONE_SAME_LOCAL_CONVERSION",
    ] = FieldInfo(alias="propertyParser")

    property_type: Literal["timepoint"] = FieldInfo(alias="propertyType")

    time_point: TimePoint = FieldInfo(alias="timePoint")

    type: str

    default_value: Optional[str] = FieldInfo(alias="defaultValue", default=None)
