# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicRangedDatePropertyOperation"]


class PublicRangedDatePropertyOperation(TypedDict, total=False):
    include_objects_with_no_value_set: Required[Annotated[bool, PropertyInfo(alias="includeObjectsWithNoValueSet")]]

    lower_bound: Required[Annotated[int, PropertyInfo(alias="lowerBound")]]

    operation_type: Required[Annotated[Literal["RANGED_DATE"], PropertyInfo(alias="operationType")]]

    operator: Required[str]

    requires_time_zone_conversion: Required[Annotated[bool, PropertyInfo(alias="requiresTimeZoneConversion")]]

    upper_bound: Required[Annotated[int, PropertyInfo(alias="upperBound")]]
