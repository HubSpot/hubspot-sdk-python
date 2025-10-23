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

    operation_type: Literal["TIME_POINT"] = FieldInfo(alias="operationType")

    operator: str

    time_point: TimePoint = FieldInfo(alias="timePoint")

    type: str

    endpoint_behavior: Optional[str] = FieldInfo(alias="endpointBehavior", default=None)

    property_parser: Optional[str] = FieldInfo(alias="propertyParser", default=None)
