# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicRangedNumberPropertyOperation"]


class PublicRangedNumberPropertyOperation(TypedDict, total=False):
    include_objects_with_no_value_set: Required[Annotated[bool, PropertyInfo(alias="includeObjectsWithNoValueSet")]]

    lower_bound: Required[Annotated[int, PropertyInfo(alias="lowerBound")]]

    operation_type: Required[Annotated[Literal["NUMBER_RANGED"], PropertyInfo(alias="operationType")]]

    operator: Required[str]

    upper_bound: Required[Annotated[int, PropertyInfo(alias="upperBound")]]
