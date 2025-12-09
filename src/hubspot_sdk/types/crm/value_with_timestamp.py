# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ValueWithTimestamp"]


class ValueWithTimestamp(BaseModel):
    """Property model that includes timestamp."""

    source_type: str = FieldInfo(alias="sourceType")
    """The property type."""

    timestamp: datetime
    """The timestamp when the property was updated, in ISO 8601 format."""

    value: str
    """The property value."""

    source_id: Optional[str] = FieldInfo(alias="sourceId", default=None)
    """The unique ID of the property."""

    source_label: Optional[str] = FieldInfo(alias="sourceLabel", default=None)
    """A human-readable label."""

    updated_by_user_id: Optional[int] = FieldInfo(alias="updatedByUserId", default=None)
    """The ID of the user who last updated the property."""
