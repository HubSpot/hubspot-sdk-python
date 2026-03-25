# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicMultiStringPropertyOperation"]


class PublicMultiStringPropertyOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")
    """
    Indicates whether objects with no value set for the property should be included
    in the operation.
    """

    operation_type: Literal["MULTISTRING"] = FieldInfo(alias="operationType")
    """Specifies the type of operation (MULTISTRING)."""

    operator: str
    """
    Defines the operation to be applied in the multi-string property operation
    (IS_EQUAL_TO, IS_NOT_EQUAL_TO, CONTAINS, CONTAINS_EXACTLY, DOES_NOT_CONTAIN,
    DOES_NOT_CONTAIN_EXACTLY, STARTS_WITH, ENDS_WITH).
    """

    values: List[str]
