# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicDatePropertyOperationParam"]


class PublicDatePropertyOperationParam(TypedDict, total=False):
    day: Required[int]
    """The day of the month for the date operation."""

    include_objects_with_no_value_set: Required[Annotated[bool, PropertyInfo(alias="includeObjectsWithNoValueSet")]]
    """
    Indicates whether objects with no value set for the property should be included.
    """

    month: Required[str]
    """The month for the date operation."""

    operation_type: Required[Annotated[Literal["DATE"], PropertyInfo(alias="operationType")]]
    """Specifies the type of operation (DATE)."""

    operator: Required[str]
    """
    Defines the operation to be applied in the date property operation
    (IS_LESS_THAN_X_DAYS_AGO, IS_MORE_THAN_X_DAYS_AGO, IS_LESS_THAN_X_DAYS_FROM_NOW,
    IS_MORE_THAN_X_DAYS_FROM_NOW).
    """

    year: Required[int]
    """The year for the date operation."""
