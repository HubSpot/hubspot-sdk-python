# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["EventDetail"]


class EventDetail(BaseModel):
    details: str
    """The details Markdown rendered as HTML."""
