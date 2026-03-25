# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicComparativeDatePropertyOperation"]


class PublicComparativeDatePropertyOperation(BaseModel):
    comparison_property_name: str = FieldInfo(alias="comparisonPropertyName")
    """The name of the property to compare against in the operation."""

    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")
    """
    Indicates whether objects with no value set for the property should be included
    in the operation.
    """

    operation_type: Literal["COMPARATIVE_DATE"] = FieldInfo(alias="operationType")
    """The type of operation (COMPARATIVE_DATE)."""

    operator: str
    """
    Defines the operation to be applied in the comparative date property operation
    (IS_BEFORE, IS_AFTER).
    """

    default_comparison_value: Optional[str] = FieldInfo(alias="defaultComparisonValue", default=None)
    """
    The default value used for comparison if the actual comparison property value is
    not set.
    """
