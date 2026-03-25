# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicDatePropertyOperation"]


class PublicDatePropertyOperation(BaseModel):
    day: int
    """The day of the month for the date operation."""

    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")
    """
    Indicates whether objects with no value set for the property should be included.
    """

    month: str
    """The month for the date operation."""

    operation_type: Literal["DATE"] = FieldInfo(alias="operationType")
    """Specifies the type of operation (DATE)."""

    operator: str
    """
    Defines the operation to be applied in the date property operation
    (IS_LESS_THAN_X_DAYS_AGO, IS_MORE_THAN_X_DAYS_AGO, IS_LESS_THAN_X_DAYS_FROM_NOW,
    IS_MORE_THAN_X_DAYS_FROM_NOW).
    """

    year: int
    """The year for the date operation."""
