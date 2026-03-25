# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MarketingEventEmailSubscriberParam"]


class MarketingEventEmailSubscriberParam(TypedDict, total=False):
    contact_properties: Required[Annotated[Dict[str, str], PropertyInfo(alias="contactProperties")]]
    """The key-value set that contains properties of the contact."""

    email: Required[str]
    """The email address of the contact in HubSpot to associate with the event."""

    interaction_date_time: Required[Annotated[int, PropertyInfo(alias="interactionDateTime")]]
    """Timestamp in milliseconds at which the contact subscribed to the event."""

    properties: Required[Dict[str, str]]
    """The key-value set that contains properties of the marketing event."""
