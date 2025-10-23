# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicDatePropertyOperation"]


class PublicDatePropertyOperation(TypedDict, total=False):
    day: Required[int]

    include_objects_with_no_value_set: Required[Annotated[bool, PropertyInfo(alias="includeObjectsWithNoValueSet")]]

    month: Required[str]

    operation_type: Required[Annotated[Literal["DATE"], PropertyInfo(alias="operationType")]]

    operator: Required[str]

    year: Required[int]
