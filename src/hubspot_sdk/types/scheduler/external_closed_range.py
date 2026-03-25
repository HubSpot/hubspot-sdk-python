# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ExternalClosedRange"]


class ExternalClosedRange(BaseModel):
    end: int
    """The end value of the closed range, represented as an integer."""

    start: int
    """The start value of the closed range, represented as an integer."""
