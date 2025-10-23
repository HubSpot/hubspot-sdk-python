# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["VisibleExternalEventTypeNames"]


class VisibleExternalEventTypeNames(BaseModel):
    event_types: List[str] = FieldInfo(alias="eventTypes")
    """List of event type names."""
