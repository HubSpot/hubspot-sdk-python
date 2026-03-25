# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .public_date_point_param import PublicDatePointParam
from .public_indexed_time_point_param import PublicIndexedTimePointParam
from .public_property_referenced_time_param import PublicPropertyReferencedTimeParam

__all__ = ["PublicTimePointOperationParam", "TimePoint"]

TimePoint: TypeAlias = Union[PublicDatePointParam, PublicIndexedTimePointParam, PublicPropertyReferencedTimeParam]


class PublicTimePointOperationParam(TypedDict, total=False):
    include_objects_with_no_value_set: Required[Annotated[bool, PropertyInfo(alias="includeObjectsWithNoValueSet")]]
    """
    Indicates whether objects with no value set for the property should be included
    in the operation.
    """

    operation_type: Required[Annotated[Literal["TIME_POINT"], PropertyInfo(alias="operationType")]]
    """Specifies the type of operation (TIME_POINT)."""

    operator: Required[str]
    """
    Specifies the operation to be applied within the time point operation
    (IS_BEFORE, IS_AFTER).
    """

    time_point: Required[Annotated[TimePoint, PropertyInfo(alias="timePoint")]]
    """
    Defines the specific point in time for the operation, which can be a date,
    indexed time, or property-referenced time.
    """

    type: Required[str]
    """Defines the type of operation being performed."""

    endpoint_behavior: Annotated[str, PropertyInfo(alias="endpointBehavior")]
    """Describes the behavior at the endpoint of the time point operation."""

    property_parser: Annotated[str, PropertyInfo(alias="propertyParser")]
    """Specifies the parser used for interpreting the property in the operation."""
