# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..marketing_event_subscriber_param import MarketingEventSubscriberParam

__all__ = ["AttendanceCreateByExternalEventIDAndContactIDParams"]


class AttendanceCreateByExternalEventIDAndContactIDParams(TypedDict, total=False):
    external_event_id: Required[Annotated[str, PropertyInfo(alias="externalEventId")]]

    inputs: Required[Iterable[MarketingEventSubscriberParam]]
    """List of HubSpot contacts to subscribe to the marketing event"""

    external_account_id: Annotated[str, PropertyInfo(alias="externalAccountId")]
    """
    The accountId that is associated with this marketing event in the external event
    application
    """
