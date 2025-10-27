# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .usage_for_object_type import UsageForObjectType

__all__ = ["CalculatedPropertyLimitResponse"]


class CalculatedPropertyLimitResponse(BaseModel):
    by_object_type: List[UsageForObjectType] = FieldInfo(alias="byObjectType")

    overall_limit: int = FieldInfo(alias="overallLimit")

    overall_percentage: float = FieldInfo(alias="overallPercentage")

    overall_usage: int = FieldInfo(alias="overallUsage")
