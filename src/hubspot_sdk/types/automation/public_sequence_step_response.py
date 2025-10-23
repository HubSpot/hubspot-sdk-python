# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_task_pattern_response import PublicTaskPatternResponse
from .public_email_pattern_response import PublicEmailPatternResponse

__all__ = ["PublicSequenceStepResponse"]


class PublicSequenceStepResponse(BaseModel):
    id: str

    action_type: str = FieldInfo(alias="actionType")

    created_at: datetime = FieldInfo(alias="createdAt")

    delay_millis: int = FieldInfo(alias="delayMillis")

    step_order: int = FieldInfo(alias="stepOrder")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    email_pattern: Optional[PublicEmailPatternResponse] = FieldInfo(alias="emailPattern", default=None)

    task_pattern: Optional[PublicTaskPatternResponse] = FieldInfo(alias="taskPattern", default=None)
