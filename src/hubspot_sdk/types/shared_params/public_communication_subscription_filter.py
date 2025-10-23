# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["PublicCommunicationSubscriptionFilter"]


class PublicCommunicationSubscriptionFilter(TypedDict, total=False):
    accepted_opt_states: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="acceptedOptStates")]]

    channel: Required[str]

    filter_type: Required[Annotated[Literal["COMMUNICATION_SUBSCRIPTION"], PropertyInfo(alias="filterType")]]

    subscription_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="subscriptionIds")]]

    subscription_type: Required[Annotated[str, PropertyInfo(alias="subscriptionType")]]

    business_unit_id: Annotated[str, PropertyInfo(alias="businessUnitId")]
