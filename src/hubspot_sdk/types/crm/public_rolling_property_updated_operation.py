# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicRollingPropertyUpdatedOperation"]


class PublicRollingPropertyUpdatedOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")
    """
    Indicates whether objects with no value set for the property should be included
    in the operation.
    """

    number_of_days: int = FieldInfo(alias="numberOfDays")
    """The number of days to be considered in the rolling property updated operation."""

    operation_type: Literal["ROLLING_PROPERTY_UPDATED"] = FieldInfo(alias="operationType")
    """Specifies the type of operation (ROLLING_PROPERTY_UPDATED)."""

    operator: str
    """
    Defines the operation to be applied within the rolling property updated
    operation (UPDATED_IN_LAST_X_DAYS, NOT_UPDATED_IN_LAST_X_DAYS).
    """
