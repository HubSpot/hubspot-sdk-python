# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MarketingEventSubscriberParam"]


class MarketingEventSubscriberParam(TypedDict, total=False):
    interaction_date_time: Required[Annotated[int, PropertyInfo(alias="interactionDateTime")]]
    """Timestamp in milliseconds at which the contact subscribed to the event."""

    properties: Required[Dict[str, str]]
    """The key-value set of the properties of the contact"""

    vid: Required[int]
    """The ID of the contact in HubSpot"""
