# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["EventDetail"]


class EventDetail(BaseModel):
    """The details Markdown rendered as HTML."""

    details: str
    """The details Markdown rendered as HTML."""
