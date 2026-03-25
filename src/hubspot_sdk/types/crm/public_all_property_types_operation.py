# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicAllPropertyTypesOperation"]


class PublicAllPropertyTypesOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")
    """Indication of whether objects with no value should be included"""

    operation_type: Literal["ALL_PROPERTY"] = FieldInfo(alias="operationType")
    """Type of operation (ALL_PROPERTY)"""

    operator: str
    """Operator to be applied (IS_KNOWN, IS_UNKNOWN)"""
