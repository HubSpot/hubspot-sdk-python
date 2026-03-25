# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ParticipationProperties"]


class ParticipationProperties(BaseModel):
    attendance_state: Literal["ATTENDED", "CANCELLED", "EMPTY", "NO_SHOW", "REGISTERED"] = FieldInfo(
        alias="attendanceState"
    )
    """The state of the participation"""

    occurred_at: int = FieldInfo(alias="occurredAt")
    """Timestamp of when the participation occurred"""

    attendance_duration_seconds: Optional[int] = FieldInfo(alias="attendanceDurationSeconds", default=None)
    """The number of seconds the participation lasted"""

    attendance_percentage: Optional[str] = FieldInfo(alias="attendancePercentage", default=None)
    """Percentage of the participation duration relative to the event duration"""
