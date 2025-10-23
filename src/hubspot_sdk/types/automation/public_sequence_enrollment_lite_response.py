# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicSequenceEnrollmentLiteResponse"]


class PublicSequenceEnrollmentLiteResponse(BaseModel):
    id: str

    enrolled_at: datetime = FieldInfo(alias="enrolledAt")

    to_email: str = FieldInfo(alias="toEmail")

    updated_at: datetime = FieldInfo(alias="updatedAt")
