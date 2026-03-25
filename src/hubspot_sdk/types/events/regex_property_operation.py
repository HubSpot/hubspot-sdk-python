# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RegexPropertyOperation"]


class RegexPropertyOperation(BaseModel):
    case_sensitive: bool = FieldInfo(alias="caseSensitive")

    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    operation_type: str = FieldInfo(alias="operationType")

    operator: Literal["DOES_NOT_MATCH_REGEX", "MATCHES_REGEX"]

    operator_name: str = FieldInfo(alias="operatorName")

    pattern: str

    property_type: Literal["regex"] = FieldInfo(alias="propertyType")

    default_value: Optional[str] = FieldInfo(alias="defaultValue", default=None)

    render_spec: Optional[str] = FieldInfo(alias="renderSpec", default=None)
