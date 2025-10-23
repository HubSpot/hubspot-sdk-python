# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SendSendParams"]


class SendSendParams(TypedDict, total=False):
    event_name: Required[Annotated[str, PropertyInfo(alias="eventName")]]
    """The internal name of the event (`pe<portalID>_eventName`).

    Can be retrieved through the
    [event definitions API](https://developers.hubspot.com/docs/reference/api/analytics-and-events/custom-events/custom-event-definitions#get-%2Fevents%2Fv3%2Fevent-definitions)
    or in
    [HubSpot's UI](https://knowledge.hubspot.com/reports/create-custom-behavioral-events-with-the-code-wizard#find-internal-name).
    """

    email: str
    """The visitor's email address.

    Used for associating the event data with a CRM record.
    """

    object_id: Annotated[str, PropertyInfo(alias="objectId")]
    """The ID of the object that completed the event (e.g., contact ID or visitor ID)."""

    occurred_at: Annotated[Union[str, datetime], PropertyInfo(alias="occurredAt", format="iso8601")]
    """The time when this event occurred.

    If this isn't set, the current time will be used.
    """

    properties: Dict[str, str]
    """The event properties to update.

    Takes the format of key-value pairs (property internal name and property value).
    Learn more about
    [HubSpot's default event properties](https://developers.hubspot.com/docs/guides/api/analytics-and-events/custom-events/custom-event-definitions#hubspot-s-default-event-properties).
    """

    utk: str
    """The visitor's usertoken. Used for associating the event data with a CRM record."""

    uuid: str
    """
    Include a universally unique identifier to assign a unique ID to the event
    completion. Can be useful for matching data between HubSpot and other external
    systems.
    """
