# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CommunicationPreferenceUpdateStatusParams"]


class CommunicationPreferenceUpdateStatusParams(TypedDict, total=False):
    channel: Required[Literal["EMAIL"]]
    """The type of communication channel, with 'EMAIL' as the only supported option."""

    status_state: Required[
        Annotated[Literal["NOT_SPECIFIED", "SUBSCRIBED", "UNSUBSCRIBED"], PropertyInfo(alias="statusState")]
    ]
    """
    The current subscription status of the contact, which can be 'SUBSCRIBED',
    'UNSUBSCRIBED', or 'NOT_SPECIFIED'.
    """

    subscription_id: Required[Annotated[int, PropertyInfo(alias="subscriptionId")]]
    """The unique identifier of the subscription to be updated."""

    legal_basis: Annotated[
        Literal[
            "CONSENT_WITH_NOTICE",
            "LEGITIMATE_INTEREST_CLIENT",
            "LEGITIMATE_INTEREST_OTHER",
            "LEGITIMATE_INTEREST_PQL",
            "NON_GDPR",
            "PERFORMANCE_OF_CONTRACT",
            "PROCESS_AND_STORE",
        ],
        PropertyInfo(alias="legalBasis"),
    ]
    """
    The legal basis for communication, with options including
    'LEGITIMATE_INTEREST_PQL', 'LEGITIMATE_INTEREST_CLIENT',
    'PERFORMANCE_OF_CONTRACT', 'CONSENT_WITH_NOTICE', 'NON_GDPR',
    'PROCESS_AND_STORE', and 'LEGITIMATE_INTEREST_OTHER'.
    """

    legal_basis_explanation: Annotated[str, PropertyInfo(alias="legalBasisExplanation")]
    """An explanation for the legal basis used for communication."""
