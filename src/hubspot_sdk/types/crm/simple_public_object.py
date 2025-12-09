# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .value_with_timestamp import ValueWithTimestamp

__all__ = ["SimplePublicObject"]


class SimplePublicObject(BaseModel):
    """A simple public object."""

    id: str
    """The unique ID of the object."""

    archived: bool
    """Whether the object is archived."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp when the object was created, in ISO 8601 format."""

    properties: Dict[str, Optional[str]]
    """Key-value pairs representing the properties of the object."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The timestamp when the object was last updated, in ISO 8601 format."""

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)
    """The timestamp when the object was archived, in ISO 8601 format."""

    object_write_trace_id: Optional[str] = FieldInfo(alias="objectWriteTraceId", default=None)
    """A unique identifier for tracing the creation request."""

    properties_with_history: Optional[Dict[str, List[ValueWithTimestamp]]] = FieldInfo(
        alias="propertiesWithHistory", default=None
    )
    """
    Key-value pairs representing the properties of the object along with their
    history.
    """

    url: Optional[str] = None
