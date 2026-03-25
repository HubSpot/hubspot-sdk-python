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
    """
    Indicates whether objects with no value set for the property should be included
    in the operation.
    """

    lower_bound_time_point: LowerBoundTimePoint = FieldInfo(alias="lowerBoundTimePoint")
    """Defines the lower bound time point for the operation."""

    operation_type: str = FieldInfo(alias="operationType")
    """Specifies the type of operation (TIME_RANGED)."""

    operator: str
    """
    Defines the operation to be applied within the time range (IS_BETWEEN,
    IS_NOT_BETWEEN).
    """

    type: Literal["TIME_RANGED"]
    """Specifies the type of operation (TIME_RANGED)."""

    upper_bound_time_point: UpperBoundTimePoint = FieldInfo(alias="upperBoundTimePoint")
    """Defines the upper bound time point for the operation."""

    lower_bound_endpoint_behavior: Optional[str] = FieldInfo(alias="lowerBoundEndpointBehavior", default=None)
    """Describes the behavior at the lower bound endpoint of the time range."""

    property_parser: Optional[str] = FieldInfo(alias="propertyParser", default=None)
    """Specifies the parser used for the property in the operation."""

    upper_bound_endpoint_behavior: Optional[str] = FieldInfo(alias="upperBoundEndpointBehavior", default=None)
    """Describes the behavior at the upper bound endpoint of the time range."""
