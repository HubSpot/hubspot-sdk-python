# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicCommunicationSubscriptionFilter"]


class PublicCommunicationSubscriptionFilter(BaseModel):
    accepted_opt_states: List[str] = FieldInfo(alias="acceptedOptStates")

    channel: str
    """
    Specifies the communication channel associated with the subscription filter
    (EMAIL, WHATSAPP, SMS).
    """

    filter_type: Literal["COMMUNICATION_SUBSCRIPTION"] = FieldInfo(alias="filterType")
    """Indicates the type of filter, which is (COMMUNICATION_SUBSCRIPTION)"""

    subscription_ids: List[str] = FieldInfo(alias="subscriptionIds")

    subscription_type: str = FieldInfo(alias="subscriptionType")
    """
    Defines the type of subscription related to the filter (PORTAL_WIDE,
    BUSINESS_UNIT_WIDE, INDIVIDUAL_SUBSCRIPTION)
    """

    business_unit_id: Optional[str] = FieldInfo(alias="businessUnitId", default=None)
    """The ID of the business unit associated with the subscription filter."""
