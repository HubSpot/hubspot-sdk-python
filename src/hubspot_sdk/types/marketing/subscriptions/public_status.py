# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["PublicStatus"]


class PublicStatus(BaseModel):
    channel: Literal["EMAIL"]
    """The type of communication channel, with 'EMAIL' as the only supported option."""

    source: str
    """The origin or method through which the subscription status was set."""

    status: Literal["NOT_SPECIFIED", "SUBSCRIBED", "UNSUBSCRIBED"]
    """
    The current subscription status of the contact, which can be 'SUBSCRIBED',
    'UNSUBSCRIBED', or 'NOT_SPECIFIED'.
    """

    subscriber_id_string: str = FieldInfo(alias="subscriberIdString")
    """The contact's email address."""

    subscription_id: int = FieldInfo(alias="subscriptionId")
    """The unique identifier of the subscription."""

    timestamp: datetime
    """The date and time when the subscription status was last updated."""

    business_unit_id: Optional[int] = FieldInfo(alias="businessUnitId", default=None)
    """The ID of the business unit associated with the subscription."""

    legal_basis: Optional[
        Literal[
            "CONSENT_WITH_NOTICE",
            "LEGITIMATE_INTEREST_CLIENT",
            "LEGITIMATE_INTEREST_OTHER",
            "LEGITIMATE_INTEREST_PQL",
            "NON_GDPR",
            "PERFORMANCE_OF_CONTRACT",
            "PROCESS_AND_STORE",
        ]
    ] = FieldInfo(alias="legalBasis", default=None)
    """
    The legal basis for communication, with options including
    'LEGITIMATE_INTEREST_PQL', 'LEGITIMATE_INTEREST_CLIENT',
    'PERFORMANCE_OF_CONTRACT', 'CONSENT_WITH_NOTICE', 'NON_GDPR',
    'PROCESS_AND_STORE', and 'LEGITIMATE_INTEREST_OTHER'.
    """

    legal_basis_explanation: Optional[str] = FieldInfo(alias="legalBasisExplanation", default=None)
    """An explanation for the legal basis used for communication."""

    set_status_success_reason: Optional[
        Literal[
            "NO_STATUS_CHANGE", "REQUESTED_CHANGE_OCCURRED", "RESUBSCRIBE_OCCURRED", "UNSUBSCRIBE_FROM_ALL_OCCURRED"
        ]
    ] = FieldInfo(alias="setStatusSuccessReason", default=None)
    """
    The reason for the successful change in subscription status, such as
    'RESUBSCRIBE_OCCURRED' or 'NO_STATUS_CHANGE'.
    """

    subscription_name: Optional[str] = FieldInfo(alias="subscriptionName", default=None)
    """The name of the subscription."""
