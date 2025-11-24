# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["PublicStatusRequestParam"]


class PublicStatusRequestParam(TypedDict, total=False):
    channel: Required[Literal["EMAIL"]]
    """The type of communication channel. Currently, only `EMAIL` is supported."""

    status_state: Required[
        Annotated[Literal["NOT_SPECIFIED", "SUBSCRIBED", "UNSUBSCRIBED"], PropertyInfo(alias="statusState")]
    ]
    """The status of the contact's subscription."""

    subscriber_id_string: Required[Annotated[str, PropertyInfo(alias="subscriberIdString")]]
    """The contact's email address."""

    subscription_id: Required[Annotated[int, PropertyInfo(alias="subscriptionId")]]
    """The ID of the subscription to update."""

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
    """The legal basis for communication."""

    legal_basis_explanation: Annotated[str, PropertyInfo(alias="legalBasisExplanation")]
    """The explanation for the legal basis."""
