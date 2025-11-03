# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .date_time import DateTime
from ...._models import BaseModel

__all__ = ["ReportCreationResponse"]


class ReportCreationResponse(BaseModel):
    enqueue_time: DateTime = FieldInfo(alias="enqueueTime")

    user_email: str = FieldInfo(alias="userEmail")

    user_id: int = FieldInfo(alias="userId")
