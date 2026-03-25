# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CommunicationPreferenceUnsubscribeParams"]


class CommunicationPreferenceUnsubscribeParams(TypedDict, total=False):
    email_address: Required[Annotated[str, PropertyInfo(alias="emailAddress")]]
    """The email address of the user whose subscription status is being updated.

    It is a required field and must be a string.
    """

    subscription_id: Required[Annotated[str, PropertyInfo(alias="subscriptionId")]]
    """The unique identifier of the subscription for which the status is being updated.

    It is a required field and must be a string.
    """

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
    """The legal basis for processing the subscription status change.

    It is an optional field and must be a string with valid values including
    'LEGITIMATE_INTEREST_PQL', 'LEGITIMATE_INTEREST_CLIENT',
    'PERFORMANCE_OF_CONTRACT', 'CONSENT_WITH_NOTICE', 'NON_GDPR',
    'PROCESS_AND_STORE', and 'LEGITIMATE_INTEREST_OTHER'.
    """

    legal_basis_explanation: Annotated[str, PropertyInfo(alias="legalBasisExplanation")]
    """An optional field providing an explanation for the legal basis used.

    It must be a string.
    """
