# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["PublicCommunicationSubscriptionFilterParam"]


class PublicCommunicationSubscriptionFilterParam(TypedDict, total=False):
    accepted_opt_states: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="acceptedOptStates")]]

    channel: Required[str]
    """
    Specifies the communication channel associated with the subscription filter
    (EMAIL, WHATSAPP, SMS).
    """

    filter_type: Required[Annotated[Literal["COMMUNICATION_SUBSCRIPTION"], PropertyInfo(alias="filterType")]]
    """Indicates the type of filter, which is (COMMUNICATION_SUBSCRIPTION)"""

    subscription_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="subscriptionIds")]]

    subscription_type: Required[Annotated[str, PropertyInfo(alias="subscriptionType")]]
    """
    Defines the type of subscription related to the filter (PORTAL_WIDE,
    BUSINESS_UNIT_WIDE, INDIVIDUAL_SUBSCRIPTION)
    """

    business_unit_id: Annotated[str, PropertyInfo(alias="businessUnitId")]
    """The ID of the business unit associated with the subscription filter."""
