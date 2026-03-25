# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicEmailPatternResponse"]


class PublicEmailPatternResponse(BaseModel):
    id: str
    """The unique identifier of the email pattern."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The date and time when the email pattern was created."""

    template_id: str = FieldInfo(alias="templateId")
    """The unique identifier of the email template associated with the pattern."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The date and time when the email pattern was last updated."""

    thread_email_to_step_order: Optional[int] = FieldInfo(alias="threadEmailToStepOrder", default=None)
    """The order identifying the previous step to which the email thread is linked."""
