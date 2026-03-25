# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PublicIndexOffset"]


class PublicIndexOffset(BaseModel):
    days: Optional[int] = None
    """The number of days to offset."""

    hours: Optional[int] = None
    """The number of hours to offset."""

    milliseconds: Optional[int] = None
    """The number of milliseconds to offset."""

    minutes: Optional[int] = None
    """The number of minutes to offset."""

    months: Optional[int] = None
    """The number of months to offset."""

    quarters: Optional[int] = None
    """The number of quarters to offset."""

    seconds: Optional[int] = None
    """The number of seconds to offset."""

    weeks: Optional[int] = None
    """The number of weeks to offset."""

    years: Optional[int] = None
    """The number of years to offset."""
