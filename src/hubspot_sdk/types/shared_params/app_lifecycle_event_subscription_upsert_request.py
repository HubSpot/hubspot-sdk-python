# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["AppLifecycleEventSubscriptionUpsertRequest"]


class AppLifecycleEventSubscriptionUpsertRequest(TypedDict, total=False):
    event_type_id: Required[Annotated[str, PropertyInfo(alias="eventTypeId")]]

    properties: Required[SequenceNotStr[str]]

    subscription_type: Required[Annotated[Literal["APP_LIFECYCLE_EVENT"], PropertyInfo(alias="subscriptionType")]]
