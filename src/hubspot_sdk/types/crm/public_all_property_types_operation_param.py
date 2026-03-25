# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicAllPropertyTypesOperationParam"]


class PublicAllPropertyTypesOperationParam(TypedDict, total=False):
    include_objects_with_no_value_set: Required[Annotated[bool, PropertyInfo(alias="includeObjectsWithNoValueSet")]]
    """Indication of whether objects with no value should be included"""

    operation_type: Required[Annotated[Literal["ALL_PROPERTY"], PropertyInfo(alias="operationType")]]
    """Type of operation (ALL_PROPERTY)"""

    operator: Required[str]
    """Operator to be applied (IS_KNOWN, IS_UNKNOWN)"""
