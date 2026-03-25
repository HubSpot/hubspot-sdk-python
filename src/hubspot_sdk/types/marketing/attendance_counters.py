# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AttendanceCounters"]


class AttendanceCounters(BaseModel):
    attended: int
    """Number of attended contact records of a marketing event"""

    cancelled: int
    """Number of cancelled contact records of a marketing event"""

    no_shows: int = FieldInfo(alias="noShows")
    """Number of no-show contact records of a marketing event"""

    registered: int
    """Number of registered contact records of a marketing event"""
