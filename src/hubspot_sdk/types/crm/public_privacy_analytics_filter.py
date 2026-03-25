# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicPrivacyAnalyticsFilter"]


class PublicPrivacyAnalyticsFilter(BaseModel):
    filter_type: Literal["PRIVACY"] = FieldInfo(alias="filterType")
    """Specifies the type of filter (PRIVACY)."""

    operator: str
    """
    Defines the operation to be applied within the filter (PRIVACY_CONSENT_GRANTED,
    PRIVACY_CONSENT_NOT_GRANTED).
    """

    privacy_name: str = FieldInfo(alias="privacyName")
    """The name of the privacy setting used in the filter."""
