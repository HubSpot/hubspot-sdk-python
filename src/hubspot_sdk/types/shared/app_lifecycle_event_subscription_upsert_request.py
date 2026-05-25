# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AppLifecycleEventSubscriptionUpsertRequest"]


class AppLifecycleEventSubscriptionUpsertRequest(BaseModel):
    event_type_id: str = FieldInfo(alias="eventTypeId")

    properties: List[str]

    subscription_type: Literal["APP_LIFECYCLE_EVENT"] = FieldInfo(alias="subscriptionType")
