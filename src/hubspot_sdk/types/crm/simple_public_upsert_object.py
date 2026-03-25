# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .value_with_timestamp import ValueWithTimestamp

__all__ = ["SimplePublicUpsertObject"]


class SimplePublicUpsertObject(BaseModel):
    """Represents a CRM object that has either been created or updated (upserted)"""

    id: str
    """The unique ID of the object."""

    archived: bool
    """Whether the object is archived."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp when the object was created, in ISO 8601 format."""

    new: bool
    """Whether the property is new."""

    properties: Dict[str, str]
    """Key value pairs representing the properties of the object."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The timestamp when the object was last updated, in ISO 8601 format."""

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)
    """The timestamp when the object was archived, in ISO 8601 format."""

    object_write_trace_id: Optional[str] = FieldInfo(alias="objectWriteTraceId", default=None)
    """An identifier used for tracing the write request for the object."""

    properties_with_history: Optional[Dict[str, List[ValueWithTimestamp]]] = FieldInfo(
        alias="propertiesWithHistory", default=None
    )
    """
    Key-value pairs representing the properties of the object along with their
    history.
    """

    url: Optional[str] = None
    """The URL associated with the object."""
