# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SubscriptionSubscribeParams"]


class SubscriptionSubscribeParams(TypedDict, total=False):
    email_address: Required[Annotated[str, PropertyInfo(alias="emailAddress")]]
    """Contact's email address."""

    subscription_id: Required[Annotated[str, PropertyInfo(alias="subscriptionId")]]
    """ID of the subscription being updated for the contact."""

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
    Legal basis for updating the contact's status (required for GDPR enabled
    portals).
    """

    legal_basis_explanation: Annotated[str, PropertyInfo(alias="legalBasisExplanation")]
    """
    A more detailed explanation to go with the legal basis (required for GDPR
    enabled portals).
    """
