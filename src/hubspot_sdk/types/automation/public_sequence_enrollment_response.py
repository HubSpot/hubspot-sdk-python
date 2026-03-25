# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicSequenceEnrollmentResponse"]


class PublicSequenceEnrollmentResponse(BaseModel):
    id: str
    """The unique identifier for the sequence enrollment."""

    enrolled_at: datetime = FieldInfo(alias="enrolledAt")
    """The date and time when the contact was enrolled in the sequence."""

    enrolled_by: str = FieldInfo(alias="enrolledBy")
    """The identifier of the user who enrolled the contact in the sequence."""

    enrolled_by_email: str = FieldInfo(alias="enrolledByEmail")
    """The email address of the user who enrolled the contact in the sequence."""

    sequence_id: str = FieldInfo(alias="sequenceId")
    """The unique identifier of the sequence in which the contact is enrolled."""

    sequence_name: str = FieldInfo(alias="sequenceName")
    """The name of the sequence in which the contact is enrolled."""

    to_email: str = FieldInfo(alias="toEmail")
    """The email address of the contact enrolled in the sequence."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The date and time when the sequence enrollment was last updated."""
