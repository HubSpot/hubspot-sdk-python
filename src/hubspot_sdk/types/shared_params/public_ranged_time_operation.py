# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .public_date_point import PublicDatePoint
from .public_indexed_time_point import PublicIndexedTimePoint
from .public_property_referenced_time import PublicPropertyReferencedTime

__all__ = ["PublicRangedTimeOperation", "LowerBoundTimePoint", "UpperBoundTimePoint"]

LowerBoundTimePoint: TypeAlias = Union[PublicDatePoint, PublicIndexedTimePoint, PublicPropertyReferencedTime]

UpperBoundTimePoint: TypeAlias = Union[PublicDatePoint, PublicIndexedTimePoint, PublicPropertyReferencedTime]


class PublicRangedTimeOperation(TypedDict, total=False):
    include_objects_with_no_value_set: Required[Annotated[bool, PropertyInfo(alias="includeObjectsWithNoValueSet")]]

    lower_bound_time_point: Required[Annotated[LowerBoundTimePoint, PropertyInfo(alias="lowerBoundTimePoint")]]

    operation_type: Required[Annotated[str, PropertyInfo(alias="operationType")]]

    operator: Required[str]

    type: Required[Literal["TIME_RANGED"]]

    upper_bound_time_point: Required[Annotated[UpperBoundTimePoint, PropertyInfo(alias="upperBoundTimePoint")]]

    lower_bound_endpoint_behavior: Annotated[str, PropertyInfo(alias="lowerBoundEndpointBehavior")]

    property_parser: Annotated[str, PropertyInfo(alias="propertyParser")]

    upper_bound_endpoint_behavior: Annotated[str, PropertyInfo(alias="upperBoundEndpointBehavior")]
