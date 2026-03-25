# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicComparativeDatePropertyOperationParam"]


class PublicComparativeDatePropertyOperationParam(TypedDict, total=False):
    comparison_property_name: Required[Annotated[str, PropertyInfo(alias="comparisonPropertyName")]]
    """The name of the property to compare against in the operation."""

    include_objects_with_no_value_set: Required[Annotated[bool, PropertyInfo(alias="includeObjectsWithNoValueSet")]]
    """
    Indicates whether objects with no value set for the property should be included
    in the operation.
    """

    operation_type: Required[Annotated[Literal["COMPARATIVE_DATE"], PropertyInfo(alias="operationType")]]
    """The type of operation (COMPARATIVE_DATE)."""

    operator: Required[str]
    """
    Defines the operation to be applied in the comparative date property operation
    (IS_BEFORE, IS_AFTER).
    """

    default_comparison_value: Annotated[str, PropertyInfo(alias="defaultComparisonValue")]
    """
    The default value used for comparison if the actual comparison property value is
    not set.
    """
