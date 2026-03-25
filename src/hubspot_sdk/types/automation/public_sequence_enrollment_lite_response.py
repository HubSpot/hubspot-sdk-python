# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicSequenceEnrollmentLiteResponse"]


class PublicSequenceEnrollmentLiteResponse(BaseModel):
    id: str
    """The unique identifier for the sequence enrollment."""

    enrolled_at: datetime = FieldInfo(alias="enrolledAt")
    """The date and time when the contact was enrolled in the sequence."""

    to_email: str = FieldInfo(alias="toEmail")
    """The email address of the contact enrolled in the sequence."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The date and time when the sequence enrollment was last updated."""
