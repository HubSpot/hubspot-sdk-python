# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_task_pattern_response import PublicTaskPatternResponse
from .public_email_pattern_response import PublicEmailPatternResponse

__all__ = ["PublicSequenceStepResponse"]


class PublicSequenceStepResponse(BaseModel):
    id: str
    """The unique identifier of the sequence step."""

    action_type: Literal["EMAIL", "FINISH_ENROLLMENT", "TASK"] = FieldInfo(alias="actionType")
    """The type of action to be performed in the sequence step."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when the sequence step was created."""

    delay_millis: int = FieldInfo(alias="delayMillis")
    """The delay in milliseconds before the sequence step is executed."""

    step_order: int = FieldInfo(alias="stepOrder")
    """The order of the step within the sequence."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The date and time when the sequence step was last updated."""

    email_pattern: Optional[PublicEmailPatternResponse] = FieldInfo(alias="emailPattern", default=None)

    task_pattern: Optional[PublicTaskPatternResponse] = FieldInfo(alias="taskPattern", default=None)
