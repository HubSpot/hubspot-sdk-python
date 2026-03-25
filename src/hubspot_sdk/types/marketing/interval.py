# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["Interval"]


class Interval(BaseModel):
    end: datetime
    """The end timestamp of the interval, in ISO8601 format."""

    start: datetime
    """The start timestamp of the interval, in ISO8601 format."""
