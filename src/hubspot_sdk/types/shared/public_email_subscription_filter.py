# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicEmailSubscriptionFilter"]


class PublicEmailSubscriptionFilter(BaseModel):
    accepted_statuses: List[str] = FieldInfo(alias="acceptedStatuses")

    filter_type: Literal["EMAIL_SUBSCRIPTION"] = FieldInfo(alias="filterType")

    subscription_ids: List[str] = FieldInfo(alias="subscriptionIds")

    subscription_type: Optional[str] = FieldInfo(alias="subscriptionType", default=None)
