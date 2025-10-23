# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicTaskPatternResponse"]


class PublicTaskPatternResponse(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    task_priority: str = FieldInfo(alias="taskPriority")

    task_type: str = FieldInfo(alias="taskType")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    notes: Optional[str] = None

    queue_id: Optional[int] = FieldInfo(alias="queueId", default=None)

    subject: Optional[str] = None

    template_id: Optional[int] = FieldInfo(alias="templateId", default=None)

    thread_email_to_step_order: Optional[int] = FieldInfo(alias="threadEmailToStepOrder", default=None)
