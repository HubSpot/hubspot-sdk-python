# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_date_point import PublicDatePoint
from .public_indexed_time_point import PublicIndexedTimePoint
from .public_property_referenced_time import PublicPropertyReferencedTime

__all__ = ["PublicRangedTimeOperation", "LowerBoundTimePoint", "UpperBoundTimePoint"]

LowerBoundTimePoint: TypeAlias = Union[PublicDatePoint, PublicIndexedTimePoint, PublicPropertyReferencedTime]

UpperBoundTimePoint: TypeAlias = Union[PublicDatePoint, PublicIndexedTimePoint, PublicPropertyReferencedTime]


class PublicRangedTimeOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    lower_bound_time_point: LowerBoundTimePoint = FieldInfo(alias="lowerBoundTimePoint")

    operation_type: str = FieldInfo(alias="operationType")

    operator: str

    type: Literal["TIME_RANGED"]

    upper_bound_time_point: UpperBoundTimePoint = FieldInfo(alias="upperBoundTimePoint")

    lower_bound_endpoint_behavior: Optional[str] = FieldInfo(alias="lowerBoundEndpointBehavior", default=None)

    property_parser: Optional[str] = FieldInfo(alias="propertyParser", default=None)

    upper_bound_endpoint_behavior: Optional[str] = FieldInfo(alias="upperBoundEndpointBehavior", default=None)
