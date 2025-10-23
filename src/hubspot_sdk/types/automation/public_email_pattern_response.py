# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicEmailPatternResponse"]


class PublicEmailPatternResponse(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    template_id: str = FieldInfo(alias="templateId")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    thread_email_to_step_order: Optional[int] = FieldInfo(alias="threadEmailToStepOrder", default=None)
