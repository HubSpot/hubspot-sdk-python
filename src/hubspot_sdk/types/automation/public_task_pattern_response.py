# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicTaskPatternResponse"]


class PublicTaskPatternResponse(BaseModel):
    id: str
    """The unique identifier for the task pattern."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when the task pattern was created."""

    task_priority: Literal["HIGH", "LOW", "MEDIUM", "NONE"] = FieldInfo(alias="taskPriority")
    """The priority level assigned to the task."""

    task_type: Literal["CALL", "EMAIL", "LINKED_IN_CONNECT", "LINKED_IN_MESSAGE", "MEETING", "TODO"] = FieldInfo(
        alias="taskType"
    )
    """The type of task, such as an email or call."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The date and time when the task pattern was last updated."""

    notes: Optional[str] = None
    """Additional notes or comments associated with the task."""

    queue_id: Optional[int] = FieldInfo(alias="queueId", default=None)
    """The identifier for the queue associated with the task."""

    subject: Optional[str] = None
    """The subject line of the task."""

    template_id: Optional[int] = FieldInfo(alias="templateId", default=None)
    """The identifier for the template used in the task."""

    thread_email_to_step_order: Optional[int] = FieldInfo(alias="threadEmailToStepOrder", default=None)
    """The order of the step to which the email thread is related."""
