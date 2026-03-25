# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .external_communication_consent_checkbox import ExternalCommunicationConsentCheckbox

__all__ = ["ExternalLegalConsentOptions"]


class ExternalLegalConsentOptions(BaseModel):
    communication_consent_checkboxes: List[ExternalCommunicationConsentCheckbox] = FieldInfo(
        alias="communicationConsentCheckboxes"
    )

    communication_consent_text: str = FieldInfo(alias="communicationConsentText")
    """The text that describes the consent for communication preferences."""

    is_legitimate_interest: bool = FieldInfo(alias="isLegitimateInterest")
    """Whether the legal basis for processing is legitimate interest."""

    legitimate_interest_subscription_types: List[int] = FieldInfo(alias="legitimateInterestSubscriptionTypes")

    privacy_policy_text: str = FieldInfo(alias="privacyPolicyText")
    """The text that describes the data processing privacy policy."""

    processing_consent_checkbox_label: str = FieldInfo(alias="processingConsentCheckboxLabel")
    """The label for the checkbox used to obtain consent for data processing."""

    processing_consent_footer_text: str = FieldInfo(alias="processingConsentFooterText")
    """The footer text accompanying the consent for data processing.

    This field is not used by the meeting platform and will always be empty.
    """

    processing_consent_text: str = FieldInfo(alias="processingConsentText")
    """The text that describes the consent for processing personal data."""

    processing_consent_type: Literal["IMPLICIT", "REQUIRED_CHECKBOX"] = FieldInfo(alias="processingConsentType")
    """The type of consent required for processing.

    Accepted values are: IMPLICIT, REQUIRED_CHECKBOX.
    """

    legitimate_interest_legal_basis: Optional[
        Literal[
            "CONSENT_WITH_NOTICE",
            "LEGITIMATE_INTEREST_CLIENT",
            "LEGITIMATE_INTEREST_OTHER",
            "LEGITIMATE_INTEREST_PQL",
            "NON_GDPR",
            "PERFORMANCE_OF_CONTRACT",
            "PROCESS_AND_STORE",
        ]
    ] = FieldInfo(alias="legitimateInterestLegalBasis", default=None)
    """The legal basis for processing under legitimate interest.

    Accepted values are: LEGITIMATE_INTEREST_PQL, LEGITIMATE_INTEREST_CLIENT,
    PERFORMANCE_OF_CONTRACT, CONSENT_WITH_NOTICE, NON_GDPR, PROCESS_AND_STORE,
    LEGITIMATE_INTEREST_OTHER.
    """
