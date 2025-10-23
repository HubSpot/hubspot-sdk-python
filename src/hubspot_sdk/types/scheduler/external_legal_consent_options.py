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

    is_legitimate_interest: bool = FieldInfo(alias="isLegitimateInterest")

    legitimate_interest_subscription_types: List[int] = FieldInfo(alias="legitimateInterestSubscriptionTypes")

    privacy_policy_text: str = FieldInfo(alias="privacyPolicyText")

    processing_consent_checkbox_label: str = FieldInfo(alias="processingConsentCheckboxLabel")

    processing_consent_footer_text: str = FieldInfo(alias="processingConsentFooterText")

    processing_consent_text: str = FieldInfo(alias="processingConsentText")

    processing_consent_type: str = FieldInfo(alias="processingConsentType")

    legitimate_interest_legal_basis: Optional[
        Literal[
            "LEGITIMATE_INTEREST_PQL",
            "LEGITIMATE_INTEREST_CLIENT",
            "PERFORMANCE_OF_CONTRACT",
            "CONSENT_WITH_NOTICE",
            "NON_GDPR",
            "PROCESS_AND_STORE",
            "LEGITIMATE_INTEREST_OTHER",
        ]
    ] = FieldInfo(alias="legitimateInterestLegalBasis", default=None)
