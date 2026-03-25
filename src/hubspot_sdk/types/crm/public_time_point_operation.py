# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_date_point import PublicDatePoint
from .public_indexed_time_point import PublicIndexedTimePoint
from .public_property_referenced_time import PublicPropertyReferencedTime

__all__ = ["PublicTimePointOperation", "TimePoint"]

TimePoint: TypeAlias = Union[PublicDatePoint, PublicIndexedTimePoint, PublicPropertyReferencedTime]


class PublicTimePointOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")
    """
    Indicates whether objects with no value set for the property should be included
    in the operation.
    """

    operation_type: Literal["TIME_POINT"] = FieldInfo(alias="operationType")
    """Specifies the type of operation (TIME_POINT)."""

    operator: str
    """
    Specifies the operation to be applied within the time point operation
    (IS_BEFORE, IS_AFTER).
    """

    time_point: TimePoint = FieldInfo(alias="timePoint")
    """
    Defines the specific point in time for the operation, which can be a date,
    indexed time, or property-referenced time.
    """

    type: str
    """Defines the type of operation being performed."""

    endpoint_behavior: Optional[str] = FieldInfo(alias="endpointBehavior", default=None)
    """Describes the behavior at the endpoint of the time point operation."""

    property_parser: Optional[str] = FieldInfo(alias="propertyParser", default=None)
    """Specifies the parser used for interpreting the property in the operation."""
