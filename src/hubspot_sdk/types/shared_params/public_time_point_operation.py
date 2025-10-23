# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .public_date_point import PublicDatePoint
from .public_indexed_time_point import PublicIndexedTimePoint
from .public_property_referenced_time import PublicPropertyReferencedTime

__all__ = ["PublicTimePointOperation", "TimePoint"]

TimePoint: TypeAlias = Union[PublicDatePoint, PublicIndexedTimePoint, PublicPropertyReferencedTime]


class PublicTimePointOperation(TypedDict, total=False):
    include_objects_with_no_value_set: Required[Annotated[bool, PropertyInfo(alias="includeObjectsWithNoValueSet")]]

    operation_type: Required[Annotated[Literal["TIME_POINT"], PropertyInfo(alias="operationType")]]

    operator: Required[str]

    time_point: Required[Annotated[TimePoint, PropertyInfo(alias="timePoint")]]

    type: Required[str]

    endpoint_behavior: Annotated[str, PropertyInfo(alias="endpointBehavior")]

    property_parser: Annotated[str, PropertyInfo(alias="propertyParser")]
