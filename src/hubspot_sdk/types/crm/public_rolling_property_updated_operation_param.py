# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicRollingPropertyUpdatedOperationParam"]


class PublicRollingPropertyUpdatedOperationParam(TypedDict, total=False):
    include_objects_with_no_value_set: Required[Annotated[bool, PropertyInfo(alias="includeObjectsWithNoValueSet")]]
    """
    Indicates whether objects with no value set for the property should be included
    in the operation.
    """

    number_of_days: Required[Annotated[int, PropertyInfo(alias="numberOfDays")]]
    """The number of days to be considered in the rolling property updated operation."""

    operation_type: Required[Annotated[Literal["ROLLING_PROPERTY_UPDATED"], PropertyInfo(alias="operationType")]]
    """Specifies the type of operation (ROLLING_PROPERTY_UPDATED)."""

    operator: Required[str]
    """
    Defines the operation to be applied within the rolling property updated
    operation (UPDATED_IN_LAST_X_DAYS, NOT_UPDATED_IN_LAST_X_DAYS).
    """
