# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .limit_and_usage_for_object_type import LimitAndUsageForObjectType

__all__ = ["CustomPropertyLimitResponse"]


class CustomPropertyLimitResponse(BaseModel):
    by_object_type: List[LimitAndUsageForObjectType] = FieldInfo(alias="byObjectType")

    overall_limit: int = FieldInfo(alias="overallLimit")

    overall_percentage: float = FieldInfo(alias="overallPercentage")

    overall_usage: int = FieldInfo(alias="overallUsage")
