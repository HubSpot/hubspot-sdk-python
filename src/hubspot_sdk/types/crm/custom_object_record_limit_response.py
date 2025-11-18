# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .usage_for_object_type import UsageForObjectType

__all__ = ["CustomObjectRecordLimitResponse"]


class CustomObjectRecordLimitResponse(BaseModel):
    by_object_type: List[UsageForObjectType] = FieldInfo(alias="byObjectType")

    overall_limit: int = FieldInfo(alias="overallLimit")
    """The maximum number of custom object records allowed."""

    overall_percentage: float = FieldInfo(alias="overallPercentage")
    """The percentage of the overall custom object record limit that has been used."""

    overall_usage: int = FieldInfo(alias="overallUsage")
    """The total number of custom object records currently in use."""
