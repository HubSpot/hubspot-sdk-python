# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DatePropertyOperation"]


class DatePropertyOperation(BaseModel):
    day: int

    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    month: Literal["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

    operation_type: str = FieldInfo(alias="operationType")

    operator: Literal["EQUAL", "BEFORE", "AFTER"]

    operator_name: str = FieldInfo(alias="operatorName")

    property_type: Literal["date"] = FieldInfo(alias="propertyType")

    year: int

    default_value: Optional[str] = FieldInfo(alias="defaultValue", default=None)
