# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicPrivacyAnalyticsFilterParam"]


class PublicPrivacyAnalyticsFilterParam(TypedDict, total=False):
    filter_type: Required[Annotated[Literal["PRIVACY"], PropertyInfo(alias="filterType")]]
    """Specifies the type of filter (PRIVACY)."""

    operator: Required[str]
    """
    Defines the operation to be applied within the filter (PRIVACY_CONSENT_GRANTED,
    PRIVACY_CONSENT_NOT_GRANTED).
    """

    privacy_name: Required[Annotated[str, PropertyInfo(alias="privacyName")]]
    """The name of the privacy setting used in the filter."""
