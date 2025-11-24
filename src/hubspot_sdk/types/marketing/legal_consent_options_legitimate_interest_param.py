# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LegalConsentOptionsLegitimateInterestParam"]


class LegalConsentOptionsLegitimateInterestParam(TypedDict, total=False):
    lawful_basis: Required[Annotated[Literal["client", "lead", "other"], PropertyInfo(alias="lawfulBasis")]]

    privacy_text: Required[Annotated[str, PropertyInfo(alias="privacyText")]]

    subscription_type_ids: Required[Annotated[Iterable[int], PropertyInfo(alias="subscriptionTypeIds")]]

    type: Required[Literal["legitimate_interest"]]
