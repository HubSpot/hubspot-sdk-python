# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExternalUnifiedEvent"]


class ExternalUnifiedEvent(BaseModel):
    id: str
    """A unique identifier for the event."""

    event_type: str = FieldInfo(alias="eventType")
    """
    The format of the `eventType` string is `ae{appId}_{eventTypeLabel}`,
    `pe{portalId}_{eventTypeLabel}`, or just `e_{eventTypeLabel}` for HubSpot
    events.
    """

    object_id: str = FieldInfo(alias="objectId")
    """The objectId of the object which did the event."""

    object_type: str = FieldInfo(alias="objectType")
    """The objectType for the object which did the event."""

    occurred_at: datetime = FieldInfo(alias="occurredAt")
    """An ISO 8601 timestamp when the event occurred."""

    properties: Optional[Dict[str, str]] = None
    """A key-value map of event-specific properties.

    The available properties depend on the event type definition.
    """
