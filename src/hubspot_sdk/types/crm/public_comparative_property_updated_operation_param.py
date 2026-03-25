# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicComparativePropertyUpdatedOperationParam"]


class PublicComparativePropertyUpdatedOperationParam(TypedDict, total=False):
    comparison_property_name: Required[Annotated[str, PropertyInfo(alias="comparisonPropertyName")]]
    """The name of the property to compare against in the operation."""

    include_objects_with_no_value_set: Required[Annotated[bool, PropertyInfo(alias="includeObjectsWithNoValueSet")]]
    """
    Indicates whether objects with no value set for the property should be included
    in the operation.
    """

    operation_type: Required[Annotated[Literal["COMPARATIVE_PROPERTY_UPDATED"], PropertyInfo(alias="operationType")]]
    """Specifies the type of operation (COMPARATIVE_PROPERTY_UPDATED)."""

    operator: Required[str]
    """
    Defines the operation to be applied, such as comparison operators (IS_BEFORE,
    IS_AFTER).
    """

    default_comparison_value: Annotated[str, PropertyInfo(alias="defaultComparisonValue")]
    """
    The default value used for comparison if the actual comparison property value is
    not set.
    """
