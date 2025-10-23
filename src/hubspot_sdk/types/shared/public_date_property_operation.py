# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicDatePropertyOperation"]


class PublicDatePropertyOperation(BaseModel):
    day: int

    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    month: str

    operation_type: Literal["DATE"] = FieldInfo(alias="operationType")

    operator: str

    year: int
