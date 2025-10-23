# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .date_point import DatePoint
from .indexed_time_point import IndexedTimePoint
from .property_referenced_time import PropertyReferencedTime

__all__ = ["RangedTimeOperation", "LowerBoundTimePoint", "UpperBoundTimePoint"]

LowerBoundTimePoint: TypeAlias = Union[DatePoint, IndexedTimePoint, PropertyReferencedTime]

UpperBoundTimePoint: TypeAlias = Union[DatePoint, IndexedTimePoint, PropertyReferencedTime]


class RangedTimeOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    lower_bound_endpoint_behavior: Literal["INCLUSIVE", "EXCLUSIVE"] = FieldInfo(alias="lowerBoundEndpointBehavior")

    lower_bound_time_point: LowerBoundTimePoint = FieldInfo(alias="lowerBoundTimePoint")

    operation_type: str = FieldInfo(alias="operationType")

    operator: Literal["IS_BETWEEN", "IS_NOT_BETWEEN"]

    operator_name: str = FieldInfo(alias="operatorName")

    property_parser: Literal[
        "VALUE",
        "UPDATED_AT",
        "ANNIVERSARY",
        "VALUE_WITH_ZONE_SAME_LOCAL_CONVERSION",
        "ANNIVERSARY_WITH_ZONE_SAME_LOCAL_CONVERSION",
    ] = FieldInfo(alias="propertyParser")

    property_type: Literal["rangedtime"] = FieldInfo(alias="propertyType")

    type: str

    upper_bound_endpoint_behavior: Literal["INCLUSIVE", "EXCLUSIVE"] = FieldInfo(alias="upperBoundEndpointBehavior")

    upper_bound_time_point: UpperBoundTimePoint = FieldInfo(alias="upperBoundTimePoint")

    default_value: Optional[str] = FieldInfo(alias="defaultValue", default=None)
