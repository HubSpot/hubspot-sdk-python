# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SmtpTokenListParams"]


class SmtpTokenListParams(TypedDict, total=False):
    after: str
    """Starting point to get the next set of results."""

    campaign_name: Annotated[str, PropertyInfo(alias="campaignName")]
    """A name for the campaign tied to the SMTP API token."""

    email_campaign_id: Annotated[str, PropertyInfo(alias="emailCampaignId")]
    """Identifier assigned to the campaign provided during the token creation."""

    limit: int
    """Maximum number of tokens to return."""
