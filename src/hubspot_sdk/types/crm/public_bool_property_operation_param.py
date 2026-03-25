# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicBoolPropertyOperationParam"]


class PublicBoolPropertyOperationParam(TypedDict, total=False):
    include_objects_with_no_value_set: Required[Annotated[bool, PropertyInfo(alias="includeObjectsWithNoValueSet")]]
    """
    Indicates whether objects with no value set for the property should be included
    in the operation.
    """

    operation_type: Required[Annotated[Literal["BOOL"], PropertyInfo(alias="operationType")]]
    """Specifies the type of operation (BOOL)."""

    operator: Required[str]
    """
    Defines the operation to be applied in the boolean property operation
    (IS_EQUAL_TO, IS_NOT_EQUAL_TO, HAS_EVER_BEEN_EQUAL_TO, HAS_NEVER_BEEN_EQUAL_TO).
    """

    value: Required[bool]
    """The boolean value to be used in the operation."""
