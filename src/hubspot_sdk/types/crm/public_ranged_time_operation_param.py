# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .public_date_point_param import PublicDatePointParam
from .public_indexed_time_point_param import PublicIndexedTimePointParam
from .public_property_referenced_time_param import PublicPropertyReferencedTimeParam

__all__ = ["PublicRangedTimeOperationParam", "LowerBoundTimePoint", "UpperBoundTimePoint"]

LowerBoundTimePoint: TypeAlias = Union[
    PublicDatePointParam, PublicIndexedTimePointParam, PublicPropertyReferencedTimeParam
]

UpperBoundTimePoint: TypeAlias = Union[
    PublicDatePointParam, PublicIndexedTimePointParam, PublicPropertyReferencedTimeParam
]


class PublicRangedTimeOperationParam(TypedDict, total=False):
    include_objects_with_no_value_set: Required[Annotated[bool, PropertyInfo(alias="includeObjectsWithNoValueSet")]]
    """
    Indicates whether objects with no value set for the property should be included
    in the operation.
    """

    lower_bound_time_point: Required[Annotated[LowerBoundTimePoint, PropertyInfo(alias="lowerBoundTimePoint")]]
    """Defines the lower bound time point for the operation."""

    operation_type: Required[Annotated[str, PropertyInfo(alias="operationType")]]
    """Specifies the type of operation (TIME_RANGED)."""

    operator: Required[str]
    """
    Defines the operation to be applied within the time range (IS_BETWEEN,
    IS_NOT_BETWEEN).
    """

    type: Required[Literal["TIME_RANGED"]]
    """Specifies the type of operation (TIME_RANGED)."""

    upper_bound_time_point: Required[Annotated[UpperBoundTimePoint, PropertyInfo(alias="upperBoundTimePoint")]]
    """Defines the upper bound time point for the operation."""

    lower_bound_endpoint_behavior: Annotated[str, PropertyInfo(alias="lowerBoundEndpointBehavior")]
    """Describes the behavior at the lower bound endpoint of the time range."""

    property_parser: Annotated[str, PropertyInfo(alias="propertyParser")]
    """Specifies the parser used for the property in the operation."""

    upper_bound_endpoint_behavior: Annotated[str, PropertyInfo(alias="upperBoundEndpointBehavior")]
    """Describes the behavior at the upper bound endpoint of the time range."""
