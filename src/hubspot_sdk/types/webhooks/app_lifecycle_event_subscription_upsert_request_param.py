# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["AppLifecycleEventSubscriptionUpsertRequestParam"]


class AppLifecycleEventSubscriptionUpsertRequestParam(TypedDict, total=False):
    event_type_id: Required[Annotated[str, PropertyInfo(alias="eventTypeId")]]

    properties: Required[SequenceNotStr[str]]

    subscription_type: Required[
        Annotated[
            Literal[
                "OBJECT", "ASSOCIATION", "EVENT", "APP_LIFECYCLE_EVENT", "LIST_MEMBERSHIP", "GDPR_PRIVACY_DELETION"
            ],
            PropertyInfo(alias="subscriptionType"),
        ]
    ]
