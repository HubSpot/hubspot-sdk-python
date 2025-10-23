# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RollingPropertyUpdatedOperation"]


class RollingPropertyUpdatedOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    number_of_days: int = FieldInfo(alias="numberOfDays")

    operation_type: str = FieldInfo(alias="operationType")

    operator: Literal["UPDATED_IN_LAST_X_DAYS", "NOT_UPDATED_IN_LAST_X_DAYS"]

    operator_name: str = FieldInfo(alias="operatorName")

    property_type: Literal["rolling-property-updated"] = FieldInfo(alias="propertyType")

    default_value: Optional[str] = FieldInfo(alias="defaultValue", default=None)
