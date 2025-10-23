# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicRollingPropertyUpdatedOperation"]


class PublicRollingPropertyUpdatedOperation(BaseModel):
    include_objects_with_no_value_set: bool = FieldInfo(alias="includeObjectsWithNoValueSet")

    number_of_days: int = FieldInfo(alias="numberOfDays")

    operation_type: Literal["ROLLING_PROPERTY_UPDATED"] = FieldInfo(alias="operationType")

    operator: str
