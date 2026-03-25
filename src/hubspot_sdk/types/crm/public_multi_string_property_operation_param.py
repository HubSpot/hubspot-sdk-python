# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["PublicMultiStringPropertyOperationParam"]


class PublicMultiStringPropertyOperationParam(TypedDict, total=False):
    include_objects_with_no_value_set: Required[Annotated[bool, PropertyInfo(alias="includeObjectsWithNoValueSet")]]
    """
    Indicates whether objects with no value set for the property should be included
    in the operation.
    """

    operation_type: Required[Annotated[Literal["MULTISTRING"], PropertyInfo(alias="operationType")]]
    """Specifies the type of operation (MULTISTRING)."""

    operator: Required[str]
    """
    Defines the operation to be applied in the multi-string property operation
    (IS_EQUAL_TO, IS_NOT_EQUAL_TO, CONTAINS, CONTAINS_EXACTLY, DOES_NOT_CONTAIN,
    DOES_NOT_CONTAIN_EXACTLY, STARTS_WITH, ENDS_WITH).
    """

    values: Required[SequenceNotStr[str]]
