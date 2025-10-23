# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicRollingPropertyUpdatedOperation"]


class PublicRollingPropertyUpdatedOperation(TypedDict, total=False):
    include_objects_with_no_value_set: Required[Annotated[bool, PropertyInfo(alias="includeObjectsWithNoValueSet")]]

    number_of_days: Required[Annotated[int, PropertyInfo(alias="numberOfDays")]]

    operation_type: Required[Annotated[Literal["ROLLING_PROPERTY_UPDATED"], PropertyInfo(alias="operationType")]]

    operator: Required[str]
