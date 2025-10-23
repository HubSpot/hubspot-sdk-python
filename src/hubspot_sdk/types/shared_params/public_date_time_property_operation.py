# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicDateTimePropertyOperation"]


class PublicDateTimePropertyOperation(TypedDict, total=False):
    include_objects_with_no_value_set: Required[Annotated[bool, PropertyInfo(alias="includeObjectsWithNoValueSet")]]

    operation_type: Required[Annotated[Literal["DATETIME"], PropertyInfo(alias="operationType")]]

    operator: Required[str]

    requires_time_zone_conversion: Required[Annotated[bool, PropertyInfo(alias="requiresTimeZoneConversion")]]

    timestamp: Required[int]
