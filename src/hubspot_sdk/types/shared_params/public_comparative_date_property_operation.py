# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicComparativeDatePropertyOperation"]


class PublicComparativeDatePropertyOperation(TypedDict, total=False):
    comparison_property_name: Required[Annotated[str, PropertyInfo(alias="comparisonPropertyName")]]

    include_objects_with_no_value_set: Required[Annotated[bool, PropertyInfo(alias="includeObjectsWithNoValueSet")]]

    operation_type: Required[Annotated[Literal["COMPARATIVE_DATE"], PropertyInfo(alias="operationType")]]

    operator: Required[str]

    default_comparison_value: Annotated[str, PropertyInfo(alias="defaultComparisonValue")]
