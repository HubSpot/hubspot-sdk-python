# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicRangedNumberPropertyOperation"]


class PublicRangedNumberPropertyOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    lower_bound: int = FieldInfo(alias="lowerBound")

    operation_type: Literal["NUMBER_RANGED"] = FieldInfo(alias="operationType")

    operator: str

    upper_bound: int = FieldInfo(alias="upperBound")
