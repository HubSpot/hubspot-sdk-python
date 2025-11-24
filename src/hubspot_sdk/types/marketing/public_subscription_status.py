# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicSubscriptionStatus"]


class PublicSubscriptionStatus(BaseModel):
    id: str
    """The ID for the subscription."""

    description: str
    """A description of the subscription."""

    name: str
    """The name of the subscription."""

    source_of_status: Literal["BRAND_WIDE_STATUS", "PORTAL_WIDE_STATUS", "SUBSCRIPTION_STATUS"] = FieldInfo(
        alias="sourceOfStatus"
    )
    """Where the status is determined from e.g.

    PORTAL_WIDE_STATUS if the contact opted out from the portal.
    """

    status: Literal["NOT_SUBSCRIBED", "SUBSCRIBED"]
    """Whether the contact is subscribed."""

    brand_id: Optional[int] = FieldInfo(alias="brandId", default=None)
    """The ID of the brand that the subscription is associated with, if there is one."""

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
    """The legal reason for the current status of the subscription."""

    legal_basis_explanation: Optional[str] = FieldInfo(alias="legalBasisExplanation", default=None)
    """A more detailed explanation to go with the legal basis."""

    preference_group_name: Optional[str] = FieldInfo(alias="preferenceGroupName", default=None)
    """The name of the preferences group that the subscription is associated with."""
