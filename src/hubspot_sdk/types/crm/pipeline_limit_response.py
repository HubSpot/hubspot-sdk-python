# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .limit_and_usage_for_object_type import LimitAndUsageForObjectType
from .custom_object_record_limit_response import CustomObjectRecordLimitResponse

__all__ = ["PipelineLimitResponse"]


class PipelineLimitResponse(BaseModel):
    custom_object_types: CustomObjectRecordLimitResponse = FieldInfo(alias="customObjectTypes")

    hubspot_defined_object_types: List[LimitAndUsageForObjectType] = FieldInfo(alias="hubspotDefinedObjectTypes")
