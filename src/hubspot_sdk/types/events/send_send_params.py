# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SendSendParams"]


class SendSendParams(TypedDict, total=False):
    event_name: Required[Annotated[str, PropertyInfo(alias="eventName")]]
    """Internal name of the event-type to trigger"""

    properties: Required[Dict[str, str]]
    """
    Map of properties for the event in the format property internal name - property
    value
    """

    email: str
    """Email of visitor"""

    object_id: Annotated[str, PropertyInfo(alias="objectId")]
    """The object id that this event occurred on.

    Could be a contact id or a visitor id.
    """

    occurred_at: Annotated[Union[str, datetime], PropertyInfo(alias="occurredAt", format="iso8601")]
    """The time when this event occurred (if any).

    If this isn't set, the current time will be used
    """

    utk: str
    """User token"""

    uuid: str
