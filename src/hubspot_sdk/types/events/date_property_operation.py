# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DatePropertyOperation"]


class DatePropertyOperation(BaseModel):
    day: int

    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    month: Literal["APR", "AUG", "DEC", "FEB", "JAN", "JUL", "JUN", "MAR", "MAY", "NOV", "OCT", "SEP"]

    operation_type: str = FieldInfo(alias="operationType")

    operator: Literal["AFTER", "BEFORE", "EQUAL"]

    operator_name: str = FieldInfo(alias="operatorName")

    property_type: Literal["date"] = FieldInfo(alias="propertyType")

    year: int

    default_value: Optional[str] = FieldInfo(alias="defaultValue", default=None)

    render_spec: Optional[str] = FieldInfo(alias="renderSpec", default=None)
