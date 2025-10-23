# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..timeline_event_i_frame_param import TimelineEventIFrameParam

__all__ = ["EventCreateParams"]


class EventCreateParams(TypedDict, total=False):
    event_template_id: Required[Annotated[str, PropertyInfo(alias="eventTemplateId")]]
    """The event template ID."""

    tokens: Required[Dict[str, str]]
    """A collection of token keys and values associated with the template tokens."""

    id: str
    """Identifier for the event.

    This is optional, and we recommend you do not pass this in. We will create one
    for you if you omit this. You can also use `{{uuid}}` anywhere in the ID to
    generate a unique string, guaranteeing uniqueness.
    """

    domain: str
    """The event domain (often paired with utk)."""

    email: str
    """The email address used for contact-specific events.

    This can be used to identify existing contacts, create new ones, or change the
    email for an existing contact (if paired with the `objectId`).
    """

    extra_data: Annotated[object, PropertyInfo(alias="extraData")]
    """
    Additional event-specific data that can be interpreted by the template's
    markdown.
    """

    object_id: Annotated[str, PropertyInfo(alias="objectId")]
    """The CRM object identifier.

    This is required for every event other than contacts (where utk or email can be
    used).
    """

    timeline_i_frame: Annotated[TimelineEventIFrameParam, PropertyInfo(alias="timelineIFrame")]

    timestamp: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The time the event occurred.

    If not passed in, the curren time will be assumed. This is used to determine
    where an event is shown on a CRM object's timeline.
    """

    utk: str
    """Use the `utk` parameter to associate an event with a contact by `usertoken`.

    This is recommended if you don't know a user's email, but have an identifying
    user token in your cookie.
    """
