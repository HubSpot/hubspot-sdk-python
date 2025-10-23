# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["EventIDView"]


class EventIDView(BaseModel):
    id: str
    """Identifier of event."""

    created: datetime
    """Time of event creation."""
