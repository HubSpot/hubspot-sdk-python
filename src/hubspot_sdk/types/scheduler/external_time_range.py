# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ExternalTimeRange"]


class ExternalTimeRange(BaseModel):
    end: int
    """The end time of the time range, represented as Unix time in milliseconds."""

    start: int
    """The start time of the time range, represented as Unix time in milliseconds."""
