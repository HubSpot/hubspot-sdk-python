# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .marketing_event_subscriber_param import MarketingEventSubscriberParam

__all__ = ["EventUpsertSubscriberStateByIDParams"]


class EventUpsertSubscriberStateByIDParams(TypedDict, total=False):
    external_event_id: Required[Annotated[str, PropertyInfo(alias="externalEventId")]]

    external_account_id: Required[Annotated[str, PropertyInfo(alias="externalAccountId")]]

    inputs: Required[Iterable[MarketingEventSubscriberParam]]
    """List of HubSpot contacts to subscribe to the marketing event"""
