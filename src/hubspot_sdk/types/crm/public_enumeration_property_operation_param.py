# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["PublicEnumerationPropertyOperationParam"]


class PublicEnumerationPropertyOperationParam(TypedDict, total=False):
    include_objects_with_no_value_set: Required[Annotated[bool, PropertyInfo(alias="includeObjectsWithNoValueSet")]]
    """
    Indicates whether objects with no value set for the property should be included
    in the operation.
    """

    operation_type: Required[Annotated[Literal["ENUMERATION"], PropertyInfo(alias="operationType")]]
    """Specifies the type of operation (ENUMERATION)."""

    operator: Required[str]
    """
    Defines the operation to be applied in the enumeration property operation
    (IS_ANY_OF, IS_NONE_OF, IS_EXACTLY, IS_NOT_EXACTLY, CONTAINS_ALL,
    DOES_NOT_CONTAIN_ALL, HAS_EVER_BEEN_ANY_OF, HAS_NEVER_BEEN_ANY_OF,
    HAS_EVER_BEEN_EXACTLY, HAS_NEVER_BEEN_EXACTLY, HAS_EVER_CONTAINED_ALL,
    HAS_NEVER_CONTAINED_ALL).
    """

    values: Required[SequenceNotStr[str]]
