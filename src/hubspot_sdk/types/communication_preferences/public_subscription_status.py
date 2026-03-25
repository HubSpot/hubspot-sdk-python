# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicSubscriptionStatus"]


class PublicSubscriptionStatus(BaseModel):
    id: str
    """The unique identifier for the subscription status."""

    description: str
    """A description of the subscription status."""

    name: str
    """The name of the subscription status."""

    source_of_status: Literal["BRAND_WIDE_STATUS", "PORTAL_WIDE_STATUS", "SUBSCRIPTION_STATUS"] = FieldInfo(
        alias="sourceOfStatus"
    )
    """
    Indicates the origin of the subscription status, with possible values being
    'PORTAL_WIDE_STATUS', 'BRAND_WIDE_STATUS', or 'SUBSCRIPTION_STATUS'.
    """

    status: Literal["NOT_SUBSCRIBED", "SUBSCRIBED"]
    """
    The current status of the subscription, which can be 'SUBSCRIBED' or
    'NOT_SUBSCRIBED'.
    """

    brand_id: Optional[int] = FieldInfo(alias="brandId", default=None)
    """
    The unique identifier for the brand associated with the subscription status,
    represented as an integer.
    """

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
    The legal basis for processing the subscription, which can include values such
    as 'LEGITIMATE_INTEREST_PQL', 'LEGITIMATE_INTEREST_CLIENT',
    'PERFORMANCE_OF_CONTRACT', 'CONSENT_WITH_NOTICE', 'NON_GDPR',
    'PROCESS_AND_STORE', or 'LEGITIMATE_INTEREST_OTHER'.
    """

    legal_basis_explanation: Optional[str] = FieldInfo(alias="legalBasisExplanation", default=None)
    """An explanation of the legal basis for the subscription status."""

    preference_group_name: Optional[str] = FieldInfo(alias="preferenceGroupName", default=None)
    """The name of the preference group associated with the subscription status."""
