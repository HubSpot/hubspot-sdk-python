# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..marketing_event_subscriber_param import MarketingEventSubscriberParam

__all__ = ["AttendanceCreateByEventIDAndContactIDParams"]


class AttendanceCreateByEventIDAndContactIDParams(TypedDict, total=False):
    object_id: Required[Annotated[str, PropertyInfo(alias="objectId")]]

    inputs: Required[Iterable[MarketingEventSubscriberParam]]
    """List of HubSpot contacts to subscribe to the marketing event"""
