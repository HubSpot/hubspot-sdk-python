# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["CustomObjectLimitResponse"]


class CustomObjectLimitResponse(BaseModel):
    limit: int
    """The maximum number of custom objects allowed."""

    percentage: float
    """The percentage of the custom object limit that is currently used."""

    usage: int
    """The current number of custom objects used."""
