# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_subscription_status import PublicSubscriptionStatus

__all__ = ["PublicSubscriptionStatusesResponse"]


class PublicSubscriptionStatusesResponse(BaseModel):
    recipient: str
    """
    The email address of the recipient for whom the subscription statuses are being
    retrieved. It is a string.
    """

    subscription_statuses: List[PublicSubscriptionStatus] = FieldInfo(alias="subscriptionStatuses")
    """
    An array of PublicSubscriptionStatus objects, each detailing the subscription
    status of the recipient for a particular subscription.
    """
