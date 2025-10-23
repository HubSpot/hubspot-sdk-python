# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicCommunicationSubscriptionFilter"]


class PublicCommunicationSubscriptionFilter(BaseModel):
    accepted_opt_states: List[str] = FieldInfo(alias="acceptedOptStates")

    channel: str

    filter_type: Literal["COMMUNICATION_SUBSCRIPTION"] = FieldInfo(alias="filterType")

    subscription_ids: List[str] = FieldInfo(alias="subscriptionIds")

    subscription_type: str = FieldInfo(alias="subscriptionType")

    business_unit_id: Optional[str] = FieldInfo(alias="businessUnitId", default=None)
