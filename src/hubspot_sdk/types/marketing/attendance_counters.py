# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AttendanceCounters"]


class AttendanceCounters(BaseModel):
    attended: int

    cancelled: int

    no_shows: int = FieldInfo(alias="noShows")

    registered: int
