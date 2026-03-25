# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BoolPropertyOperation"]


class BoolPropertyOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    operation_type: str = FieldInfo(alias="operationType")

    operator: Literal["HAS_EVER_BEEN_EQUAL_TO", "HAS_NEVER_BEEN_EQUAL_TO", "IS_EQUAL_TO", "IS_NOT_EQUAL_TO"]

    operator_name: str = FieldInfo(alias="operatorName")

    property_type: Literal["bool"] = FieldInfo(alias="propertyType")

    value: bool

    default_value: Optional[str] = FieldInfo(alias="defaultValue", default=None)

    render_spec: Optional[str] = FieldInfo(alias="renderSpec", default=None)
