# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["PublicEmailSubscriptionFilterParam"]


class PublicEmailSubscriptionFilterParam(TypedDict, total=False):
    accepted_statuses: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="acceptedStatuses")]]

    filter_type: Required[Annotated[Literal["EMAIL_SUBSCRIPTION"], PropertyInfo(alias="filterType")]]
    """Indicates the type of filter (EMAIL_SUBSCRIPTION)."""

    subscription_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="subscriptionIds")]]

    subscription_type: Annotated[str, PropertyInfo(alias="subscriptionType")]
    """
    The type of subscription related to the filter (PORTAL, BRAND, SUBSCRIPTION,
    HARDBOUNCE, SPAMREPORT).
    """
