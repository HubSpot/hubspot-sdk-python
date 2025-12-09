# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .timeline_event_i_frame import TimelineEventIFrame

__all__ = ["TimelineEventResponse"]


class TimelineEventResponse(BaseModel):
    """The current state of the timeline event."""

    id: str
    """Identifier for the event.

    This should be unique to the app and event template. If you use the same ID for
    different CRM objects, the last to be processed will win and the first will not
    have a record. You can also use `{{uuid}}` anywhere in the ID to generate a
    unique string, guaranteeing uniqueness.
    """

    event_template_id: str = FieldInfo(alias="eventTemplateId")
    """The event template ID."""

    object_type: str = FieldInfo(alias="objectType")
    """The ObjectType associated with the EventTemplate."""

    tokens: Dict[str, str]
    """A collection of token keys and values associated with the template tokens."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    domain: Optional[str] = None
    """The event domain (often paired with utk)."""

    email: Optional[str] = None
    """The email address used for contact-specific events.

    This can be used to identify existing contacts, create new ones, or change the
    email for an existing contact (if paired with the `objectId`).
    """

    extra_data: Optional[object] = FieldInfo(alias="extraData", default=None)
    """
    Additional event-specific data that can be interpreted by the template's
    markdown.
    """

    object_id: Optional[str] = FieldInfo(alias="objectId", default=None)
    """The CRM object identifier.

    This is required for every event other than contacts (where utk or email can be
    used).
    """

    timeline_i_frame: Optional[TimelineEventIFrame] = FieldInfo(alias="timelineIFrame", default=None)

    timestamp: Optional[datetime] = None
    """The time the event occurred.

    If not passed in, the curren time will be assumed. This is used to determine
    where an event is shown on a CRM object's timeline.
    """

    utk: Optional[str] = None
    """Use the `utk` parameter to associate an event with a contact by `usertoken`.

    This is recommended if you don't know a user's email, but have an identifying
    user token in your cookie.
    """
