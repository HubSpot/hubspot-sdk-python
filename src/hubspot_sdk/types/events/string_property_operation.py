# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["StringPropertyOperation"]


class StringPropertyOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    operation_type: str = FieldInfo(alias="operationType")

    operator: Literal[
        "IS_EQUAL_TO",
        "IS_NOT_EQUAL_TO",
        "CONTAINS",
        "DOES_NOT_CONTAIN",
        "STARTS_WITH",
        "ENDS_WITH",
        "HAS_EVER_BEEN_EQUAL_TO",
        "HAS_NEVER_BEEN_EQUAL_TO",
        "HAS_EVER_CONTAINED",
        "HAS_NEVER_CONTAINED",
    ]

    operator_name: str = FieldInfo(alias="operatorName")

    property_type: Literal["string"] = FieldInfo(alias="propertyType")

    value: str

    default_value: Optional[str] = FieldInfo(alias="defaultValue", default=None)
